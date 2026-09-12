from app.saas.billing.models import Invoice
class BillingService:
    def generate_invoice(self, tid: str, amt: float) -> Invoice: return Invoice(tid, amt)
