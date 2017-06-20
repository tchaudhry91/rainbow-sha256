#!/usr/bin/env python

import hasher
import os
import flask
import redis

REDIS_HOST = "localhost"
REDIS_CONNECTION = None
app = flask.Flask(__name__)

"""Get the hexdigest for the given string"""
def get_hash_digest(unicode_string):
    return hasher.get_SHA256_digest(unicode_string)


"""Perform a put to redis for the given key/value pair"""
def put_to_redis(key, value):
    global REDIS_CONNECTION
    REDIS_CONNECTION.set(key, value)


"""Perform a get on redis"""
def get_from_redis(key):
    global REDIS_CONNECTION
    return REDIS_CONNECTION.get(key)


"""HTTP handler for /hash"""
@app.route('/hash')
def hash():
    unicode_string = flask.request.args['str']
    hash = get_hash_digest(unicode_string)
    put_to_redis(hash, unicode_string)
    return hash

"""HTTP handler for /reverse_hash"""
@app.route('/reverse_hash')
def reverse_hash():
    hash = flask.request.args['str']
    unicode_string = get_from_redis(hash)
    if unicode_string == None:
        return "Not Found"
    else:
        return unicode_string

"""Start Flask App and initialize"""
def main():
    global REDIS_CONNECTION
    REDIS_CONNECTION = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)
    app.run(host="0.0.0.0")


if __name__=="__main__":
    main()
