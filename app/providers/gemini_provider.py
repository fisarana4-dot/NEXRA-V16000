import os,json,urllib.request
class GeminiProvider:
 def __init__(s):s.key=os.getenv("GEMINI_API_KEY");s.model="gemini-3.6-flash"
 def generate(s,p):
  u="https://generativelanguage.googleapis.com/v1beta/models/"+s.model+":generateContent"
  d=json.dumps({"contents":[{"parts":[{"text":p}]}]}).encode()
  r=urllib.request.Request(u,data=d,headers={"x-goog-api-key":s.key,"Content-Type":"application/json"})
  with urllib.request.urlopen(r)as x:return json.load(x)
gemini_provider=GeminiProvider()
