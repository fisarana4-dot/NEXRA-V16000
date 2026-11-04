from app.core.ai_fusion.providers.azure import AzureProvider
def test_azure_not_configured():
    assert AzureProvider().status()["status"]=="NOT_CONFIGURED"
from app.providers.registry.provider_router import router
def test_azure_router():
    assert router.route("azure").status()["provider"]=="azure"
