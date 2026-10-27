import sqlite3
import app.rag.retriever as retriever
from app.rag.service import retrieve_context
def test_rag_retrieval(tmp_path):
    retriever.DB = str(tmp_path / "evidence.db")
    conn = sqlite3.connect(retriever.DB)
    conn.execute("CREATE TABLE evidence(id,source,domain,data)")
    conn.execute("INSERT INTO evidence VALUES(1,'TRADINGVIEW','GOLD','{}')")
    conn.commit()
    result=retrieve_context("GOLD",2)
    assert "SOURCE=TRADINGVIEW" in result
    assert "DOMAIN=GOLD" in result
