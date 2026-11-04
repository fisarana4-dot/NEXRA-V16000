from gateway.router.failover import DynamicAIRouter, ModelNode
def test_router():
    n = ModelNode(provider='google', model_name='gemini')
    r = DynamicAIRouter([n]); assert r.route('test') != {}
