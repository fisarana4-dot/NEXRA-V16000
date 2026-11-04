from pydantic import BaseModel,field_validator
from typing import Literal
from app.trading.gold.core.engine_ids import M15_ENGINE,M1_ENGINE
class CaseRecord(BaseModel):
 engine_id:str
 score:int=0
 m15_approved:bool=False
 direction:Literal["BUY","SELL"]="BUY"
 tp:float=0
 entry:float=0
 sl:float=0
 decision:Literal["BUY","SELL","NO_TRADE"]
 @field_validator("engine_id")
 @classmethod
 def valid_engine(cls,v):
  if v not in (M15_ENGINE,M1_ENGINE):raise ValueError("Invalid engine")
  return v
