import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')) 
channel = connection.channel() 

channel.queue_declare(queue='hello') 

#In our case this callback function will print on the screen the contents of the message.
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body) 

#We need to tell RabbitMQ that this particular callback function should receive messages from our hello queue:
channel.basic_consume(queue='hello',
                      on_message_callback=callback, 
                      auto_ack=True) 

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()