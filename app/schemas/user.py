from pydantic import BaseModel, EmailStr, Field, ConfigDict
from app.models.user import UserRole

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

