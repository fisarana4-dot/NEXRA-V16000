from app.saas.tenants.service import TenantService
def test_create(): s = TenantService(); assert s.create("Acme").name == "Acme"
