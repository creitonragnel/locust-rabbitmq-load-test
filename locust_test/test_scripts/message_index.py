from dotenv import load_dotenv
from json import dumps
from logging import info
from locust import TaskSet, task
from pathlib import Path

from .helpers.message_index_json import create_message
from helpers.hash import create_hash

ROUTING_KEY = "lightyear"
NAME = "Index Message RabbitMQ With Locust"


class MessageIndex(TaskSet):
    def on_stop(self):
        self.client.disconnect()

    @task
    def send_message(self):
        message = dumps(create_message(create_hash()))
        response = self.client.publish(
            NAME,
            ROUTING_KEY,
            message,
        )
        info(f"Index Message RabbitMQ With Locust: {response}")
