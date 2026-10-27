from datetime import datetime
from sqlalchemy import String,DateTime,func
from sqlalchemy.orm import Mapped,mapped_column
from app.core.database import Base
class Lead(Base):
    __tablename__="leads"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    tenant_id:Mapped[str]=mapped_column(String(100),index=True,nullable=False)
    company_name:Mapped[str]=mapped_column(String(255),nullable=False)
    country:Mapped[str|None]=mapped_column(String(100))
    industry:Mapped[str|None]=mapped_column(String(150))
    website:Mapped[str|None]=mapped_column(String(500))
    email:Mapped[str|None]=mapped_column(String(255))
    phone:Mapped[str|None]=mapped_column(String(50))
    source:Mapped[str|None]=mapped_column(String(255))
    verification_status:Mapped[str]=mapped_column(String(50),default="UNVERIFIED")
    lead_score:Mapped[int]=mapped_column(default=0,nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now())
