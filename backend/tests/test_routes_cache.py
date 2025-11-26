import pytest
from fastapi import status

from app.services import redis as redis_service


class FakeRedis:
    def __init__(self) -> None:
        self.store = {}

    def set(self, k, v) -> None:
        self.store[k] = v

    def get(self, k):
        return self.store.get(k, None)


@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    fake = FakeRedis()
    monkeypatch.setattr(redis_service, "redis_client", fake)
    return fake


@pytest.mark.skip(reason="Redis not running yet")
def test_cache_test(client):
    response = client.get("/api/cache/cache-test")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert "cached_value" in data
    assert data["cached_value"] == "Hello, Redis!"
