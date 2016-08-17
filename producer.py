import time
import pika

params = pika.URLParameters('amqp://worker:password@queue/task/')
connection = pika.BlockingConnection(params)
channel = connection.channel()

queue = channel.queue_declare(durable=True, exclusive=True, auto_delete=True)
reply_to = queue.method.queue
print(reply_to)

channel.basic_publish(exchange='amq.topic',
                      routing_key='search',
                      body='Hello World!',
                      properties=pika.BasicProperties(reply_to=reply_to))

time.sleep(10)
