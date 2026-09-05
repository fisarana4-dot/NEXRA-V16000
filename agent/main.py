import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("NEXRA Gemini Agent: READY")
while True:
    q=input("NEXRA> ")
    if q.lower() in ("exit","quit"): break
    print("Received:",q)
    r=client.models.generate_content(model="gemini-flash-latest",contents=q)
    print("Gemini:",r.text)
