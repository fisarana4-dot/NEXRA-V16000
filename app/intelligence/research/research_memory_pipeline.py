from typing import List, TypeVar, Generic, Optional, Any, Dict
from datetime import datetime, timezone

T = TypeVar('T')

class MemoryItem:
    """Represents a structured, typed item in the research memory pipeline."""
    def __init__(
        self,
        content: Any,
        timestamp: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        self.content: Any = content
        self.timestamp: datetime = timestamp or datetime.now(timezone.utc)
        self.metadata: Dict[str, Any] = metadata or {}

    def __repr__(self) -> str:
        return f"MemoryItem(content={repr(self.content)}, timestamp={self.timestamp.isoformat()}, metadata={self.metadata})"


class MemoryPipeline(Generic[T]):
    def __init__(self, limit: int = 5) -> None:
        """Initialize the pipeline with a safe limit.
        
        Args:
            limit: The maximum number of items to keep in the pipeline. Must be a positive integer.
        """
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError("Limit must be an integer")
        if limit <= 0:
            raise ValueError("Limit must be a positive integer greater than zero")
            
        self.limit: int = limit
        self.summary: str = ""
        self.items: List[T] = []

    def add(self, item: T) -> None:
        """Add a typed item to the pipeline, maintaining the limit.
        
        Args:
            item: The item to add to the pipeline.
        """
        self.items.append(item)
        if len(self.items) > self.limit:
            self.items = self.items[-self.limit:]

    def clear(self) -> None:
        """Clear all items and reset summary."""
        self.items = []
        self.summary = ""

    def recent(self, n: Optional[int] = None) -> List[T]:
        """Get the n most recent items. If n is None, returns all items.
        
        Args:
            n: Optional number of recent items to return. Must be a positive integer if provided.
            
        Returns:
            A list of the most recent items (up to n).
        """
        if n is None:
            return list(self.items)
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n must be an integer")
        if n <= 0:
            raise ValueError("n must be a positive integer")
        return list(self.items[-n:])
