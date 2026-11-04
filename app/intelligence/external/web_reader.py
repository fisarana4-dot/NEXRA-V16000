import requests
def fetch(url):
 r=requests.get(url,timeout=10); return r.status_code,len(r.text)
from dataclasses import dataclass
@dataclass
class WebResult:
 status:int; length:int; title:str=""; text:str=""
 length:int
