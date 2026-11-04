from dataclasses import dataclass
@dataclass
class Diagnostic:
    event_id: str
    trace_id: str
    component: str
    status: str
    message: str
