from helpers.rabbitmq_user import RabbitMQUser
from locust import constant, LoadTestShape
from test_scripts.message_index import MessageIndex


class AmqpUser(RabbitMQUser):
    wait_time = constant(0.5)
    weight = 100
    tasks = [MessageIndex]


class StagesShape(LoadTestShape):

    stages = [
        {"duration": 60, "users": 2, "spawn_rate": 1},
        {"duration": 120, "users": 4, "spawn_rate": 2},
        {"duration": 180, "users": 6, "spawn_rate": 3},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
