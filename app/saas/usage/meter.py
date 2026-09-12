from app.saas.usage.models import UsageRecord
class UsageMeter:
 def track(self, time: str, tokens: int) -> UsageRecord: return UsageRecord(time, tokens)
