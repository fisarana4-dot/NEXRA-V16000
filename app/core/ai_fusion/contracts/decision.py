from pydantic import BaseModel

class Decision(BaseModel):
    status: str
    provider: str
    answer: str
