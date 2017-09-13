#!/usr/bin/env python

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
        for word in words_file.read().split('\n'):
            counter += 1
            formatted_url = URL + '{}'.format(word)
            requests.get(formatted_url)
            if counter == COUNTER:
                counter = 0
                speed = (time.time() - time_start)
                print("Seconds per {} requests = {}".format(counter, speed))
                time_start = time.time()


if __name__ == "__main__":
    IP = sys.argv[1]
    PORT = sys.argv[2]
    URL = 'http://{}:{}/hash?str='.format(IP, PORT)
    COUNTER = int(sys.argv[3])
    main()
