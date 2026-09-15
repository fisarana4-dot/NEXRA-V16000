from dataclasses import dataclass
@dataclass
class Candidate:
    name:str
    location:str=''
    source:str=''
    url:str=''
    evidence:dict|None=None
