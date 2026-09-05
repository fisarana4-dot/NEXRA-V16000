import sqlite3
def log(a,t,s,x):
 c=sqlite3.connect("ledger/performance_ledger.db");c.execute("insert into ai_runs(ai,task,status,score)values(?,?,?,?)",(a,t,s,x));c.commit()
