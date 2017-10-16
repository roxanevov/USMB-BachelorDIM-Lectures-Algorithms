# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:07:57 2017

@author: vovardr
"""

import argparse
import subprocess
parser = argparse.ArgumentParser()
parser.add_argument("-read", action="store_true", help="read message")
parser.add_argument("-concurrency", action="store_true",help="activate persistent")
#parser.add_argument("--number",help="nombre de messages envoyé")
args = parser.parse_args().read
argConcurrency = parser.parse_args().concurrency
#argNumber=parser.parse_args().number
if args :
    execfile('simple_queue_read.py')
else:
    execfile('simple_queue_publish.py')

i=0
if argConcurrency :
    while i<10:
        subprocess.call('py -2 simple_queue_publish.py -concurrency', shell=True)       
        i=i+1