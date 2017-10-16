# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:04:48 2017

@author: vovardr
"""

# consume.py
import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://paissqpu:e0dPXbF2vE0J1twC7IW53wBUWTe_mqj5@lark.rmq.cloudamqp.com/paissqpu')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.queue_declare(queue='presentation')

def callback(ch, method, properties, body):
  print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='presentation',
                      no_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()