#!/usr/bin/env python

import grequests
import requests
import sys
import time

WORDS_FILE = "words/words.txt"
DELIMITER = "\n"
IP = ""
URL = "" 
COUNTER = 10


# Read the file and thrust word requests to the server to save
def main():
    with open(WORDS_FILE, 'r') as words_file:
        counter = 0
        time_start = time.time()
        buff_urls = []
        for word in words_file.read().split('\n'):
            counter += 1
            formatted_url = URL + '{}'.format(word)
            buff_urls.append(formatted_url)
            if counter == COUNTER:
                counter = 0
                rs = (grequests.get(u) for u in buff_urls)
                map_urls = grequests.map(rs)
                failures = 0
                serv_failures = 0
                for code in map_urls:
                    if not isinstance(code, requests.models.Response):
                        failures += 1
                    elif code.status_code != 200:
                        serv_failures += 1
                print("Request Failures: {}".format(failures))
                print("Response Code Failures: {}".format(serv_failures))
                buff_urls = []
                speed = (time.time() - time_start)
                print("Seconds per {} requests = {}".format(COUNTER, speed))
                time_start = time.time()


if __name__ == "__main__":
    IP = sys.argv[1]
    PORT = sys.argv[2]
    URL = 'http://{}:{}/hash?str='.format(IP, PORT)
    COUNTER = int(sys.argv[3])
    main()
