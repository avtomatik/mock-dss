from datetime import datetime

from fastapi import status


def test_sign_endpoint(client):
    payload = {"document_id": "doc2718", "payload": "Hello world!"}

    response = client.post("/api/sign", json=payload)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["document_id"] == payload["document_id"]
    assert "signature_value" in data
    datetime.fromisoformat(data["signed_at"])
