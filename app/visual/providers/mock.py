class MockVisualProvider:
 def generate(self,request): return {"ok":True,"kind":request["kind"]}
