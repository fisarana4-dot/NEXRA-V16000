from app.saas.billing.service import BillingService
def test_billing(): s = BillingService(); i = s.generate_invoice("t1", 99.9); assert i.amount == 99.9
