class RiskGovernor:
 def allow(self,d):
  if d.get("power_fail"):return False
  if d.get("blocked"):return False
  if d.get("decision")=="NO_TRADE":return False
  return True
risk_governor=RiskGovernor()
