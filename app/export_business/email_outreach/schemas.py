from pydantic import BaseModel, EmailStr
class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    from_email: EmailStr | None = None
    reply_to: EmailStr | None = None
