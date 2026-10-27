from pydantic import BaseModel
from typing import Optional
class LeadCreate(BaseModel):
    tenant_id:str
    company_name:str
    country:Optional[str]=None
    industry:Optional[str]=None
    website:Optional[str]=None
    email:Optional[str]=None
    phone:Optional[str]=None
    source:Optional[str]=None
class LeadResponse(LeadCreate):
    id:int
    verification_status:str="UNVERIFIED"
    lead_score:int=0
    created_at:Optional[str]=None
