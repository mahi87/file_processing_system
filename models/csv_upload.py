
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base


class CSVUpload(Base):
    __tablename__ = "csv_uploads"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user=Column(String(255), nullable=False)
    blob_address=Column(String, nullable=False)
    status=Column(String)
    created_at=Column(DateTime(timezone=True), server_default=func.now())