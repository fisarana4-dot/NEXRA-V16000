import pytest
from datetime import datetime, timezone
from app.intelligence.research.research_memory_pipeline import MemoryPipeline, MemoryItem

def test_memory_item_initialization():
    """Verify MemoryItem initializes correctly with content, timestamp, and metadata."""
    item = MemoryItem(content="test_content", metadata={"source": "pytest"})
    assert item.content == "test_content"
    assert isinstance(item.timestamp, datetime)
    assert item.metadata == {"source": "pytest"}

def test_pipeline_default_limit():
    """Verify MemoryPipeline initializes with a default limit of 5."""
    pipeline = MemoryPipeline()
    assert pipeline.limit == 5
    assert pipeline.summary == ""
    assert pipeline.items == []

def test_pipeline_custom_limit():
    """Verify MemoryPipeline initializes correctly with a custom valid limit."""
    pipeline = MemoryPipeline(limit=10)
    assert pipeline.limit == 10

def test_pipeline_invalid_limit_types():
    """Verify limit validation raises TypeError for non-integer types."""
    with pytest.raises(TypeError, match="Limit must be an integer"):
        MemoryPipeline(limit="5")  # string
    with pytest.raises(TypeError, match="Limit must be an integer"):
        MemoryPipeline(limit=5.5)  # float
    with pytest.raises(TypeError, match="Limit must be an integer"):
        MemoryPipeline(limit=True)  # boolean (subclass of int)
    with pytest.raises(TypeError, match="Limit must be an integer"):
        MemoryPipeline(limit=None)  # None

def test_pipeline_invalid_limit_values():
    """Verify limit validation raises ValueError for non-positive values."""
    with pytest.raises(ValueError, match="Limit must be a positive integer greater than zero"):
        MemoryPipeline(limit=0)
    with pytest.raises(ValueError, match="Limit must be a positive integer greater than zero"):
        MemoryPipeline(limit=-10)

def test_pipeline_add_respects_limit():
    """Verify that adding items honors the configured limit and drops oldest."""
    pipeline = MemoryPipeline[str](limit=3)
    
    pipeline.add("A")
    assert pipeline.items == ["A"]
    
    pipeline.add("B")
    pipeline.add("C")
    assert pipeline.items == ["A", "B", "C"]
    
    # Adding past the limit
    pipeline.add("D")
    assert pipeline.items == ["B", "C", "D"]

def test_pipeline_clear():
    """Verify clear() empties the items list and resets the summary."""
    pipeline = MemoryPipeline[int](limit=5)
    pipeline.summary = "A brief summary of events"
    pipeline.add(1)
    pipeline.add(2)
    
    assert len(pipeline.items) == 2
    assert pipeline.summary == "A brief summary of events"
    
    pipeline.clear()
    assert pipeline.items == []
    assert pipeline.summary == ""

def test_pipeline_recent_all():
    """Verify recent(None) or recent() returns all items in chronological order."""
    pipeline = MemoryPipeline[str](limit=5)
    for char in ["A", "B", "C"]:
        pipeline.add(char)
        
    assert pipeline.recent() == ["A", "B", "C"]
    assert pipeline.recent(None) == ["A", "B", "C"]

def test_pipeline_recent_n():
    """Verify recent(n) returns up to n most recent items in chronological order."""
    pipeline = MemoryPipeline[str](limit=5)
    for char in ["A", "B", "C", "D"]:
        pipeline.add(char)
        
    assert pipeline.recent(1) == ["D"]
    assert pipeline.recent(2) == ["C", "D"]
    assert pipeline.recent(10) == ["A", "B", "C", "D"]  # safe out-of-bounds n

def test_pipeline_recent_invalid_arguments():
    """Verify recent(n) raises TypeError/ValueError for invalid inputs."""
    pipeline = MemoryPipeline[str](limit=5)
    pipeline.add("A")
    
    with pytest.raises(TypeError, match="n must be an integer"):
        pipeline.recent("1")
    with pytest.raises(TypeError, match="n must be an integer"):
        pipeline.recent(1.5)
    with pytest.raises(TypeError, match="n must be an integer"):
        pipeline.recent(True)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        pipeline.recent(0)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        pipeline.recent(-3)

def test_pipeline_with_typed_memory_items():
    """Verify the pipeline works correctly with structured MemoryItem types."""
    pipeline = MemoryPipeline[MemoryItem](limit=2)
    item1 = MemoryItem("Task 1 completed", metadata={"importance": "high"})
    item2 = MemoryItem("Task 2 started")
    item3 = MemoryItem("Task 3 pending")
    
    pipeline.add(item1)
    pipeline.add(item2)
    pipeline.add(item3)
    
    recent_items = pipeline.recent()
    assert len(recent_items) == 2
    assert recent_items[0].content == "Task 2 started"
    assert recent_items[1].content == "Task 3 pending"
    assert isinstance(recent_items[0].timestamp, datetime)
