from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String

from app.services.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, index=True)
    signed_at = Column(DateTime, default=datetime.now(timezone.utc))
    signature_value = Column(String)
