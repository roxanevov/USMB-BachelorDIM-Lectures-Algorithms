# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:45:08 2017

@author: vovardr
"""

# consume.py
import pika, os

import argparse

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://paissqpu:e0dPXbF2vE0J1twC7IW53wBUWTe_mqj5@lark.rmq.cloudamqp.com/paissqpu')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
count=0
result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue

corr_id = str(uuid.uuid4())
channel.basic_publish(exchange='',
                           routing_key='rpc_queue',
                           properties=pika.BasicProperties(
                                 reply_to = callback_queue,
                                 correlation_id = corr_id,),
                           body=request_msg)

response=None
def on_response(ch, method, props, body):
    if corr_id == props.correlation_id:
        global response
        response=str(body)

print('Starting to wait on the response queue')
channel.basic_consume(on_response, no_ack=True,
                      queue=callback_queue)
while response is None: # wait for an answer
    connection.process_data_events()
connection.close()
