class BaseProvider:
 name="base"
 def status(self): return {"provider":self.name}
 def ask(self,text): raise NotImplementedError
