from dataclasses import dataclass
@dataclass
class Order:
 direction:str;entry:float;sl:float;qty:float
 reason:str="";trail:bool=False
