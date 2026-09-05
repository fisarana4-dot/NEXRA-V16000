from app.visual.schemas.visual_request import validate
class VisualEngine:
 def __init__(self,registry): self.registry=registry
 def generate(self,kind,prompt,provider):
  if not validate(kind,prompt): return None
