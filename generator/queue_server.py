import pika
from generator import converter
import base64
import json


def run(host='localhost', port=5672, queue='generator_queue'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))

    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')

    def on_request(ch, method, props, body):
        json_model = body
        print(" [.] processing {}".format(json.loads(json_model)['email']))

        result_path = converter.render_pdf('dummy.jade', json_model)
        with open(result_path, 'rb') as f:
            response = base64.b64encode(f.read())

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
                             correlation_id=props.correlation_id),
                         body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='rpc_queue')

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()


if __name__ == "__main__":
    run()
