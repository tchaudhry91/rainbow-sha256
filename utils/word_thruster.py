#!/usr/bin/env python

import requests
import sys

WORDS_FILE = "words/words.txt"
DELIMITER = "\n"
IP = "127.0.0.1"
URL = 'http://localhost:9999/hash?str='


# Read the file and thrust word requests to the server to save
def main():
    with open(WORDS_FILE, 'r') as words_file:
        for word in words_file.read().split('\n'):
            formatted_url = URL + '{}'.format(word)
            print(formatted_url)
            requests.get(formatted_url)


if __name__ == "__main__":
    IP = sys.argv[1]
    main()
