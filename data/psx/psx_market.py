import requests
x=requests.get("https://dps.psx.com.pk/market-watch").text
print(len(x))