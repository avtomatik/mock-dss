import json

import pika

from app.core.config import settings


def get_rabbitmq_connection():
    return pika.BlockingConnection(pika.URLParameters(settings.mq_url))


def publish_message(queue: str, message: dict):
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=queue,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2),
    )

    print(f"Sent message to queue '{queue}': {message}")
    connection.close()


def consume_messages(queue: str):
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    def callback(channel, method, properties, body):
        message = json.loads(body)
        print(f"Received message from queue '{queue}': {message}")

        # Placeholder

        channel.basic_ack(delivery_tag=method.delivery_tag)

    print(f"Waiting for message from queue '{queue}'...")
    channel.basic_consume(queue=queue, on_message_callback=callback)
    channel.start_consuming()
