import sqlite3,time
from app.trading.scout.live_gold import price
c=sqlite3.connect("nexra_research.db");p=price();c.execute("INSERT INTO market_observations(ts,price) VALUES(?,?)",(time.time(),p));c.commit();print(p)
