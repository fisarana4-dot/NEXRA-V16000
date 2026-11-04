from .models import EmailMessage
class EmailService:
    def __init__(self, transport):
        self.transport = transport
    def send(self, message: EmailMessage):
        return self.transport.send(message)
