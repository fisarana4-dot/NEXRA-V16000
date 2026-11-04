from app.core.settings import settings

class OpenAIClient:
    def __init__(self):
        self.model = settings.OPENAI_MODEL

openai_client = OpenAIClient()
