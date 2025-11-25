import redis

from app.core.config import settings

redis_client = redis.StrictRedis.from_url(settings.redis_url)


def test_redis_connection():
    try:
        redis_client.ping()
        print("Redis connection successful.")
    except redis.ConnectionError:
        print("Failed to connect to Redis.")
        raise
