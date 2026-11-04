from .models import EmailMessage
class EmailTransport:
    def send(self, message: EmailMessage):
        raise NotImplementedError
class MockEmailTransport(EmailTransport):
    def __init__(self):
        self.sent = []
    def send(self, message: EmailMessage):
        self.sent.append(message)
        return {"status": "sent", "to": message.to}
