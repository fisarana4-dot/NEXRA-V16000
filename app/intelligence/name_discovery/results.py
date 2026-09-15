from dataclasses import dataclass
@dataclass
class SearchResult:
    title:str
    url:str
    snippet:str=""
    source:str=""
    timestamp:str=""
    score:float=0.0
