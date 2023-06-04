from helpers.rabbitmq_user import RabbitMQUser
from locust import constant
from test_scripts.message_index import MessageIndex


class AmqpUser(RabbitMQUser):
    wait_time = constant(0.5)
    weight = 100
    tasks = [MessageIndex]
