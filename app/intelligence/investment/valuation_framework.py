class ValuationFramework: pass
def roe(p,e): return p/e*100 if e else 0
def roe_trend(r): return r[-1]-r[0] if len(r)>1 else 0
def dupont(m,t,l): return m*t*l
def growth(n,o): return (n/o-1)*100 if o else 0
def fcf_yield(f,mc): return f/mc*100 if mc else 0
def debt_ratio(d,e): return d/e if e else 0
def pe(eps,p): return p/eps if eps else 0
def pb(bvps,p): return p/bvps if bvps else 0
def div_yield(d,p): return d/p*100 if p else 0
def fair_value(eps,pe): return eps*pe
def margin(fv,p): return (fv-p)/fv*100 if fv else 0
def risk(debt,roe,g): return debt*50-roe-g
def decision(m,roe,risk): return "BUY" if m>=20 and roe>=15 and risk<20 else "HOLD"
def signal(m,roe,risk): return "SELL" if m<0 or risk>=50 else decision(m,roe,risk)
def analyze(d): return {"roe":roe(d["p"],d["e"]),"growth":growth(d["e"],d["oe"]),"signal":signal(d["m"],d["roe"],d["risk"])}
