from app.core.config import settings
def test_redis_url_exists():
 assert settings.REDIS_URL
