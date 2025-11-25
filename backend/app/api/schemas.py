from datetime import datetime

from pydantic import BaseModel


class SignRequest(BaseModel):
    document_id: str
    payload: str


class SignResponse(BaseModel):
    signature_id: str
    document_id: str
    signed_at: datetime
    signature_value: str
