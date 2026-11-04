from dataclasses import dataclass
@dataclass
class Evidence:
 source:str; domain:str; data:dict; timestamp:str; provenance:dict|None=None
