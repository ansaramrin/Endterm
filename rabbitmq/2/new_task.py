import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
#MAKING BASIC CONNECTIONS
#PARAMETER 'DURABLE' SAVES ALL MESSAGES ON QUEUE

#MESSAGE WHICH WILL CONTAIN ALL THE STUFF WHICH IS WRITTEN AFTER 'new_task.py' IN TERMINAL
message = ' '.join(sys.argv[1:]) or "Hello World!"
#DELIVERING MESSAGE TO QUEUE
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()