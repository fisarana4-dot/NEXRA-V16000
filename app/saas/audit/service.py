from app.saas.audit.models import AuditLog
class AuditService:
    def log(self, act: str, tid: str) -> AuditLog: return AuditLog(act, tid)
