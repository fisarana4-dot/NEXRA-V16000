from app.providers.registry.provider_router import router
def test_router(): assert router.route("gemini").name=="gemini"
