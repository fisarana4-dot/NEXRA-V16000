import requests
def price(): return requests.get("https://xaus.com/api/v1/spot", timeout=10).json()["xau"]["price"]

