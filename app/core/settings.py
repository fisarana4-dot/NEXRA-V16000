import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    SYSTEM_NAME='NEXRA V16000'
    OPENAI_MODEL=os.getenv("OPENAI_MODEL","gpt-6.1-sol")
settings=Settings()
