import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
#FANOUT TYPE EXCHANGE BROADCAST ALL THE MESSAGES IT RECEIVES
#TO ALL THE QUEUES IT KNOWS


#MAKING A NEW QUEUE WITH A RANDOM NAME
#AFTER THE CONSUMER CONNECTION IS CLOSED, QUEUE WILL BE DELETED BY PARAMETER exclusive
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#BINDING(связывающий) EXCHANGES AND QUEUE
#'result.method.queue' STORES(хранить) THE NAME OF RANDOM NAMED QUEUE
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()