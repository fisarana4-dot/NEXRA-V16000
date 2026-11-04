from app.core.ai_fusion.health.provider_health import choose,chain
from app.core.ai_fusion.skills.coding_skill import CodingSkill
from app.core.ai_fusion.providers.gemini import GeminiProvider
from app.providers.registry.provider_router import router
from app.providers.registry.provider_registry import provider_registry
class AIRouter:
 def __init__(self):self.registry=provider_registry;self.selected=choose(chain());self.provider=router.route(self.selected)
 def route(self,n,t): return CodingSkill().execute(t) if n=="coding" else {"s":"OK","p":self.selected,"r":self.provider.ask(t) or "GEMINI_UNAVAILABLE"} if n=="reasoning" else {"s":"NOT_CONNECTED"} if n in self.registry.capabilities else {"s":"NO"}
