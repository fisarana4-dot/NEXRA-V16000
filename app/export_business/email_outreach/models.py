from dataclasses import dataclass
from typing import Optional

@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str
    from_email: Optional[str] = None
    reply_to: Optional[str] = None
