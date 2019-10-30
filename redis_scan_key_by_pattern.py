#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
  扫描指定正则表达式的key
'''
__author__ = "liaojiacan"

import redis
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--host",
    type=str,
    required=True,
    help="Redis host.")
parser.add_argument(
    "--port",
    type=int,
    default="6379",
    help="Redis port.")

parser.add_argument(
    "--database",
    type=int,
    default="0",
    help="Redis database.")

parser.add_argument(
    'pattern',
    help="key pattern for scan."
)

parser.add_argument(
    'batch_size',
    type=int,
    default=1000,
    help="bath_size at one time."
)
argv = parser.parse_args()
batch_size = argv.batch_size

r = redis.Redis(host=argv.host, port=argv.port,db=argv.database, decode_responses=True)
cursor_number = 0

while True:
    cursor_number, keys = r.execute_command(
        'scan', cursor_number, "match", argv.pattern, "count", batch_size)
    if cursor_number == '0':
        break
    for key in keys:
        print(key)
