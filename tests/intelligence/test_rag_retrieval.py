from app.rag.service import retrieve_context
def test_rag_retrieval():
    result=retrieve_context("GOLD",2)
    assert "SOURCE=TRADINGVIEW" in result
    assert "DOMAIN=GOLD" in result
