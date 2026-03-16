from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from database import Base

class Content(Base):
    __tablename__ = "content"
    
    id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    serial_number= Column(String(255), unique=True, nullable=False)
    sku_id=Column(String(255), nullable=False)
    variant_type=Column(String(255), nullable=False)
    sku_name=Column(String(255), nullable=False)
    price=Column(Integer, nullable=False)
    qty=Column(Integer, nullable=False)
    store_location=Column(String(255), nullable=False)
    