import pytest
from fastapi import status

from app.api.schemas import SignRequest


def test_api_root_exists(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "Digital Signature Service" in response.text


@pytest.mark.skip(reason="Redis & RabbitMQ are not running yet")
def test_api_smoke_endpoints(client):
    assert client.get("/api/cache/cache-test").status_code in (
        status.HTTP_200_OK,
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
    assert client.post(
        "api/mq/sign-async",
        json=SignRequest(document_id="x", payload="y").model_dump(),
    ).status_code in (
        status.HTTP_200_OK,
        status.HTTP_422_UNPROCESSABLE_CONTENT,
    )


def test_openapi_lists_expected_tags(client):
    spec = client.get("/openapi.json").json()

    tags = {
        t
        for path in spec["paths"].values()
        for method in path.values()
        for t in method.get("tags", [])
    }

    assert {"sign", "cache", "rabbitmq"} <= tags
