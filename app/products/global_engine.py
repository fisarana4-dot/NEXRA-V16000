from app.autonomy.research.providers import ask

def research(product):
    return ask("Global product research: "+product)
from app.products.scoring import score

def opportunity(demand,margin,competition,risk):
    return score(demand,margin,competition,risk)

def analyze(product,demand,margin,competition,risk):
    return {"research":research(product),"score":opportunity(demand,margin,competition,risk)}
from app.products.metrics import metrics,safe
def auto_score(product):
 m=metrics(product)
 return opportunity(**safe(m))
from app.products.metrics import business
def safe_score(product):
 m=business(metrics(product))
 return opportunity(**m) if m else 50
