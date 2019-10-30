#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
   给指定模式的key设置ttl
'''
__author__ = "liaojiacan"

import redis
import argparse
from random import randint

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
    'ttl',
    metavar='ttl', 
    type=int, 
    nargs='+',
    help="ttl range "
)

argv = parser.parse_args()
ttl_range = argv.ttl
ttl_min = ttl_range[0]
ttl_max = ttl_range[0] if len(ttl_range) == 1 else ttl_range[1]

r = redis.Redis(host=argv.host, port=argv.port,db=argv.database, decode_responses=True)
cursor_number = 0
pipe = r.pipeline()

while True:
    cursor_number, keys = r.execute_command(
        'scan', cursor_number, "match", argv.pattern, "count", 5000)

    for key in keys:
        ttl = randint(ttl_min, ttl_max)
        pipe.expire(key,ttl)
        print("EXPIRE ", key , ttl)
    if len(keys) > 0 :
        pipe.execute()               
    if cursor_number == '0':
        break