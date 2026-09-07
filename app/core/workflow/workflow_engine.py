class WorkflowEngine:
 def __init__(self):
  self.states={}
 def define(self,name,steps):
  self.states[name]=steps
  return name
 def run(self,name,context=None):
  c=context or {}
  for s in self.states.get(name,[]): c=s(c)
  return c
