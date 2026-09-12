from dataclasses import dataclass
@dataclass
class Invoice: tenant_id: str; amount: float; status: str = "unpaid"
