import time
import pika

params = pika.URLParameters('amqp://worker:password@queue/task/')
connection = pika.BlockingConnection(params)
channel = connection.channel()

queue = channel.queue_declare(durable=True, exclusive=True, auto_delete=True)
reply_to = queue.method.queue
# channel.queue_bind(exchange='', queue=reply_to)
print(reply_to)

if channel.basic_publish(exchange='',
                         routing_key='search',
                         body='Hello World!',
                         properties=pika.BasicProperties(reply_to=reply_to)):
    print('Message publish was confirmed')
else:
    print('Message could not be confirmed')


# time.sleep(50)
