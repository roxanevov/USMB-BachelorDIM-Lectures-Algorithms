# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:04:48 2017

@author: vovardr
"""

# consume.py
import pika, os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-concurrency', action='store_true', help='activate persistent')
argsConcurrency = parser.parse_args().concurrency

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://paissqpu:e0dPXbF2vE0J1twC7IW53wBUWTe_mqj5@lark.rmq.cloudamqp.com/paissqpu')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
count=0
channel.queue_declare(queue='presentation')

def callback(ch, method, properties, body):
  global count
  count=count+1
  print("Nombre de messages lu %r"% count)
  print(" [x] Received %r" % body)

    if argsConcurrency :
        channel.basic_consume(callback,
                              queue='presentation'
                              )
    else:
        channel.basic_consume(callback,
                              queue='presentation',
                              no_ack=True)
print(' [*] Waiting for messages:')
channel.start_consuming()