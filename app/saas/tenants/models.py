from dataclasses import dataclass, field
import uuid
@dataclass
class Tenant:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
