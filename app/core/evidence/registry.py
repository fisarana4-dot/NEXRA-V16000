class SourceRegistry:
 def __init__(self): self._sources={}
 def register(self,n,c): self._sources[n]=c
 def get(self,n): return self._sources.get(n)
 def all(self): return dict(self._sources)
