import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.schemas import SignRequest, SignResponse
from app.dependencies import get_db
from app.models.document import Document, Signature

router = APIRouter()


@router.get("/ping")
async def ping():
    return {"status": "ok"}


@router.post("/", response_model=SignResponse)
async def sign_document(request: SignRequest, db: Session = Depends(get_db)):
    fake_signature = str(uuid.uuid4()).replace("-", "")
    signature_id = str(uuid.uuid4())

    new_document = Document(
        document_id=request.document_id, content=request.payload
    )
    db.add(new_document)
    db.commit()

    new_signature = Signature(
        signature_id=signature_id,
        document_id=request.document_id,
        signed_at=datetime.now(timezone.utc),
        signature_value=f"mock-signature-{fake_signature}",
    )
    db.add(new_signature)
    db.commit()

    return SignResponse(
        signature_id=signature_id,
        document_id=request.document_id,
        signed_at=datetime.now(timezone.utc),
        signature_value=f"mock-signature-{fake_signature}",
    )
