import time, typing
from pydantic import BaseModel
class ModelNode(BaseModel):
    provider: str
    model_name: str
class DynamicAIRouter:
    def __init__(self, nodes): self.nodes = nodes
    def route(self, p):
        return {'status': 'SUCCESS', 'model': self.nodes[0].model_name}
