import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#DIRECT TYPE EXCHANGE BROADCAST MESSAGES TO QUEUES WITH THE SAME ROUTING_KEY
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

#MAKING A NEW QUEUE WITH A RANDOM NAME
#AFTER THE CONSUMER CONNECTION IS CLOSED, QUEUE WILL BE DELETED BY PARAMETER exclusive
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#ASSIGNING THE ROUTING KEY
severities = sys.argv[1:]

#IF NOTHING ENTERED AFTER PROGRAMM NAME WE WILL POP THIS TO THE SCREEN
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

#BINDING EXCHANGES AND QUEUE
for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()