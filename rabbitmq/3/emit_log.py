import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
#FANOUT TYPE EXCHANGE BROADCAST(передавать) ALL THE MESSAGES IT RECEIVES
#TO ALL THE QUEUES IT KNOWS

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
#MESSAGE WHICH WILL CONTAIN ALL THE STUFF WHICH IS WRITTEN AFTER 'emit_log.py' IN TERMINAL
channel.basic_publish(exchange='logs', routing_key='', body=message)
#PUBLISHING TO EXCHANGE
print(" [x] Sent %r" % message)
connection.close()