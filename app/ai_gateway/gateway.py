from app.ai_gateway.provider_router import router
class AIGateway:
 def process(s,p,r):return router.route(p).ask(r)
gateway=AIGateway()
