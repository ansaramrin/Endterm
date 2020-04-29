import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#DIRECT TYPE EXCHANGE BROADCAST MESSAGES TO QUEUES WITH THE SAME ROUTING_KEY
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

#IF INFO IS MAJOR WE WILL ADD IT
severity = sys.argv[1] if len(sys.argv) > 2 else 'info'

#MESSAGE WHICH WILL CONTAIN ALL THE STUFF WHICH IS WRITTEN AFTER 'emit_log_direct.py' IN TERMINAL
message = ' '.join(sys.argv[2:]) or 'Hello World!'

#PUBLISHING TO EXCHANGE,
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()