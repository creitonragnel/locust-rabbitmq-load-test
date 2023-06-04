from datetime import datetime
from locust import events, User
import logging
import pika
from pika.exceptions import AMQPConnectionError, AMQPError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) - 30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class RabbitMQClient:
    _connected = False

    def connect(self):
        params = "localhost"

        try:
            self._connection = pika.BlockingConnection(
                pika.ConnectionParameters(params)
            )
            self._channel = self._connection.channel()
            self._connected = True
        except AMQPConnectionError as e:
            logging.error(e)

    def publish(self, scenario_name, routing_key, message, request_type="AMQP"):
        if not self._connected:
            self.connect()

        try:
            watch = StopWatch()
            watch.start()
            resp = self._channel.basic_publish(
                exchange="", routing_key=routing_key, body=message
            )
            watch.stop()
        except AMQPError as e:
            watch.stop()
            events.request_failure.fire(
                request_type=request_type,
                name=scenario_name,
                response_time=watch.elapsed_time(),
                exception=e,
            )
        else:
            events.request_success.fire(
                request_type=request_type,
                name=scenario_name,
                response_time=watch.elapsed_time(),
                response_length=0,
            )
        return resp

    def close_channel(self):
        if self._channel is not None:
            LOGGER.info("Closing the channel")
            self._channel.close()

    def close_connection(self):
        if self._connection is not None:
            LOGGER.info("Closing connection")
            self._connection.close()

    def disconnect(self):
        self.close_channel()
        self.close_connection()
        self._connected = False


class StopWatch:
    def start(self):
        self._start = datetime.now()

    def stop(self):
        self._end = datetime.now()

    def elapsed_time(self):
        timedelta = self._end - self._start
        return timedelta.total_seconds() * 1000


class RabbitMQUser(User):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(RabbitMQUser, self).__init__(*args, **kwargs)
        self.client = RabbitMQClient()
        self.client._locust_environment = self.environment
