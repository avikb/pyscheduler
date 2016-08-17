import time
import pika

params = pika.URLParameters('amqp://worker:password@queue/task/')
connection = pika.BlockingConnection(params)
channel = connection.channel()


import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

msg = id_generator()

queue = channel.queue_declare(durable=True, exclusive=True, auto_delete=True)
reply_to = queue.method.queue
# print(reply_to)

channel.basic_publish(exchange='amq.topic',
                      routing_key='search',
                      body=msg,
                      properties=pika.BasicProperties(reply_to=reply_to))
print('send: '+msg)


def callback(ch, method, properties, body):
    ch.stop_consuming()
    print('receive: ' + str(body))

channel.basic_consume(callback, queue=reply_to, no_ack=True)


def on_timeout(channel, method, properties, body):
    channel.stop_consuming()

connection.add_timeout(5, on_timeout)
channel.start_consuming()
