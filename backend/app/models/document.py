from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, func

from app.services.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, unique=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, server_default=func.now())


class Signature(Base):
    __tablename__ = "signatures"

    id = Column(Integer, primary_key=True, index=True)
    signature_id = Column(String, unique=True)
    document_id = Column(String, index=True)
    signed_at = Column(DateTime, index=True)
    signature_value = Column(String)
