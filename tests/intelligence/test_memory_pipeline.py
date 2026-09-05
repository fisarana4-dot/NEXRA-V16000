from app.intelligence.research.research_memory_pipeline import MemoryPipeline
def test_memory():
 m=MemoryPipeline(2)
 [m.add(x) for x in "ABC"];assert m.items==["B","C"]
