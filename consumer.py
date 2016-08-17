import time
import pika


params = pika.URLParameters('amqp://worker:password@queue/task/')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def on_message(channel, method, props, body):
    print(method, props, body)
    channel.basic_publish('', props.reply_to, str(body) + '-ret')
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message, 'search')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
