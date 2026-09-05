import sqlite3
DB="nexra_evidence.db"
def init():
 c=sqlite3.connect(DB)
 c.execute("CREATE TABLE IF NOT EXISTS evidence(id INTEGER PRIMARY KEY,source TEXT,domain TEXT,data TEXT,timestamp TEXT,provenance TEXT,hash TEXT)")
 c.commit();c.close()
import json
def save(e,h):
 c=sqlite3.connect(DB)
 c.execute("INSERT INTO evidence(source,domain,data,timestamp,provenance,hash) VALUES(?,?,?,?,?,?)",(e.source,e.domain,json.dumps(e.data),e.timestamp,json.dumps(e.provenance),h))
 c.commit();c.close()
def recent(n=10):
 c=sqlite3.connect(DB);r=c.execute("SELECT * FROM evidence ORDER BY id DESC LIMIT ?",(n,)).fetchall();c.close();return r
