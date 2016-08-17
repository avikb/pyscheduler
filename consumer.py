import time
import pika

params = pika.URLParameters('amqp://worker:password@queue/task/')
connection = pika.BlockingConnection(params)
channel = connection.channel()


while True:
    try:
        ok, prop, msg = channel.basic_get(queue='search')
        print(ok, prop, msg)
        res = channel.basic_publish('', prop.reply_to, msg)
        print(res)
        channel.basic_ack(ok.delivery_tag)
    except AttributeError:
        time.sleep(2)
