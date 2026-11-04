import sqlite3
DB="nexra_evidence.db"
def search(query,limit=5):
 conn=sqlite3.connect(DB)
 rows=conn.execute("SELECT * FROM evidence WHERE source LIKE ? OR domain LIKE ? OR data LIKE ? ORDER BY id DESC LIMIT ?",
 (f"%{query}%",f"%{query}%",f"%{query}%",limit)).fetchall()
 conn.close()
 return rows
