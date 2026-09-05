SOURCES={}
def register(name,domain,kind,capabilities=None): SOURCES[name]={"domain":domain,"kind":kind,"capabilities":capabilities or []}
from .sources import register
register("TRADINGVIEW","GOLD","webhook",["signals","indicators"])
register("MT5","GOLD","bridge",["market","account","positions","orders"])
register("XAUS","GOLD","api",["spot","intraday"])
