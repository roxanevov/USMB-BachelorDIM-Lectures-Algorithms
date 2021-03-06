# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:53:15 2017

@author: vovardr
"""

import pika, os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-concurrency', action='store_true', help='activate persistent')
argsConcurrency = parser.parse_args().concurrency

url = os.environ.get('CLOUDAMQP_URL','amqp://paissqpu:e0dPXbF2vE0J1twC7IW53wBUWTe_mqj5@lark.rmq.cloudamqp.com/paissqpu')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='presentation') # Declare a queue

if argsConcurrency :
    channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='Hello CloudAMQP!',
                      properties=pika.BasicProperties(
                      delivery_mode = 2, # make message persistent
                      ))
    print(" [x] Sent 'Hello World concurrency!'")
else :
    channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='Hello CloudAMQP!')

    print(" [x] Sent 'Hello World!'")

connection.close()