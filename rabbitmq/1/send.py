import pika

#We are connecting to a broker on the local machine - hence the localhost.
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel() 

#Create a hello queue to which the message will be delivered
channel.queue_declare(queue='hello') 

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()