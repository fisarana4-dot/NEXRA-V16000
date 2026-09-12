from app.saas.rbac.models import Role
from app.saas.rbac.service import RBACService
def test_rbac(): r = Role("admin", ["read", "write"]); s = RBACService(); assert s.has_permission(r, "read")
