from .base import SourceAdapter
class AdapterRegistry:
 def __init__(self): self._a={}
 def add(self,n,a): self._a[n]=a
 def get(self,n): return self._a.get(n)
 def all(self): return dict(self._a)
