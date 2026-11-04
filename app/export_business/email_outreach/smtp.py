import os
import smtplib
from email.message import EmailMessage as MIMEEmail
from .models import EmailMessage
from .transports import EmailTransport
class SMTPEmailTransport(EmailTransport):
 def __init__(self,host=None,port=None,user=None,password=None,from_email=None,tls=True):
  self.host=host or os.getenv("SMTP_HOST")
  self.port=int(port or os.getenv("SMTP_PORT","587"));self.user=user or os.getenv("SMTP_USERNAME")
  self.password=password or os.getenv("SMTP_PASSWORD")
  self.from_email=from_email or os.getenv("SMTP_FROM_EMAIL")
  self.tls=tls
 def send(self,message: EmailMessage):
  if not self.host or not self.from_email:
   return {"status":"NOT_CONFIGURED"}
  mail=MIMEEmail()
  mail["From"]=message.from_email or self.from_email
  mail["To"]=message.to;mail["Subject"]=message.subject
  if message.reply_to: mail["Reply-To"]=message.reply_to
  mail.set_content(message.body)
  with smtplib.SMTP(self.host,self.port) as server:
   if self.tls: server.starttls()
   if self.user and self.password: server.login(self.user,self.password)
   server.send_message(mail)
  return {"status":"sent","to":message.to}
