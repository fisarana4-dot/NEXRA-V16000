

import os
import httpx
from .base.base_provider import BaseProvider

class AzureProvider(BaseProvider):
    name = "azure"

    def __init__(self):
        self.endpoint = os.getenv("AZURE_OPENAI_ENDP
