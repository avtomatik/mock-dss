from datetime import datetime

from fastapi import status

from app.api.schemas import SignRequest


def test_sign_endpoint(client):
    payload = SignRequest(document_id="doc2718", payload="Hello world!")

    response = client.post("/api/sign", json=payload.model_dump())
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    for key in ["signature_id", "document_id", "signed_at", "signature_value"]:
        assert key in data
    assert data["document_id"] == payload.document_id
    assert "signature_value" in data
    datetime.fromisoformat(data["signed_at"])
