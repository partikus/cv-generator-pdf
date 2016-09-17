import beanstalkc
from generator import converter
import base64
import json


def run(host='localhost', port=14711):
    connection = beanstalkc.Connection(host=host, port=port)
    connection.watch('todo')
    connection.use('done')

    print(" [x] Awaiting RPC requests")

    while True:
        job = connection.reserve()
        json_model = job.body

        print(" [.] processing {}".format(json.loads(json_model)['email']))

        result_path = converter.render_pdf('dummy.jade', json_model)
        with open(result_path, 'rb') as f:
            response = json.dumps(
                {'id': job.jid, 'body': base64.b64encode(f.read()).decode('utf-8')})

        connection.put(response)
        job.delete()


if __name__ == "__main__":
    run()
