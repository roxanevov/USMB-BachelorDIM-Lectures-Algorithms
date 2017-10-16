# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:07:57 2017

@author: vovardr
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-read", action="store_true", help="read message")
args = parser.parse_args().read

if args :
    execfile('simple_queue_read.py')
else:
    execfile('simple_queue_publish.py')

