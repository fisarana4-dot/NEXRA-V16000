from app.saas.tenants.models import Tenant
class TenantService:
    def __init__(self): self.t = {}
    def create(self, name): t = Tenant(name=name); self.t[t.id] = t; return t
