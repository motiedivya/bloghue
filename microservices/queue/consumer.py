import sys
print(sys.path)
import pynsq
from config import settings

def message_handler(message):
    print(f"Received message: {message.body.decode()}")
    return True

def listen_to_messages():
    reader = pynsq.Reader(
        message_handler=message_handler,
        lookupd_http_addresses=[settings.nsq_lookupd_url],
        topic=settings.topic_name,
        channel="microservice_channel"
    )
    pynsq.run()

if __name__ == "__main__":
    listen_to_messages()
