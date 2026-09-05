DOMAINS={}
def register(name,kind): DOMAINS[name]=kind
from .domains import register
register("GOLD","TRADING")
register("STOCKS","TRADING")
register("COMMODITIES","TRADING")
register("AMAZON","BUSINESS")
register("SUPPORT","BUSINESS")
