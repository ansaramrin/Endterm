import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
#DECLARING QUEUE, CONNECTING TO LOCALHOST AND QUEUE, MAKING QUEUE DURABLE
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.')) #WAITS [COUNT OF DOTS IN THE MESSAGE] SECONDS
    print(" [x] Done") #IF AND ONLY IF MESSAGE IS DONE, RABBITMQ CAN DELETE IT FROM THE QUEUE
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1) #RABBITMQ WILL NOT GIVE THE MESSAGE TO CONSUMER IF IT IS BUSY
channel.basic_consume(queue='task_queue', on_message_callback=callback) #CONSUMING FUNCTION

channel.start_consuming()