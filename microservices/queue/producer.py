import pynsq
from queue.config import settings

def publish_message(message: str):
    writer = pynsq.Writer([settings.nsq_writer_url])

    def send_message():
        writer.pub(settings.topic_name, message.encode(), callback=print_response)

    def print_response(conn, data):
        print(f"Response: {data}")

    pynsq.run(send_message)
