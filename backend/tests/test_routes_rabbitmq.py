import pytest
from fastapi import status

from app.api.schemas import SignRequest
from app.services import rabbitmq as rabbitmq_service


@pytest.fixture
def mock_publish_message(monkeypatch):
    calls = []

    def fake_publish(queue, message):
        calls.append((queue, message))

    monkeypatch.setattr(rabbitmq_service, "publish_message", fake_publish)
    return calls


@pytest.mark.skip(reason="RabbitMQ not running yet")
def test_sign_async(client, mock_publish_message):
    payload = SignRequest(document_id="doc2718", payload="Hello world!")

    response = client.post("/api/mq/sign-async", json=payload.model_dump())
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data["status"] == "queued"

    assert len(mock_publish_message) == 1

    queue, message = mock_publish_message[0]
    assert queue == "signing_queue"
    assert message["document_id"] == "doc2718"
    assert message["payload"] == "Hello world!"
    assert "timestamp" in message
    assert "signature_id" in message
