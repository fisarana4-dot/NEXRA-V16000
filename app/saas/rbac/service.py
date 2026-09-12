from app.saas.rbac.models import Role
class RBACService:
    def has_permission(self, role: Role, perm: str) -> bool: return perm in role.permissions
