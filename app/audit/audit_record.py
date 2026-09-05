class AuditRecord:
 def __init__(self,name,status,rule="R0",severity="INFO",evidence=""):
  self.name=name;self.status=status;self.rule=rule;self.severity=severity
  self.evidence=evidence
  self.engine_id=""
  self.decision=""
  self.score=0
  self.entry=0
  self.sl=0
  self.tp=0
