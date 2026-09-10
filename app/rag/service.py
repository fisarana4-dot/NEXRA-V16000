from app.rag.retriever import search
from app.rag.context import build
def retrieve_context(query,limit=5):
 return build(search(query,limit))
