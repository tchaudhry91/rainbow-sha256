#!/usr/bin/env python

import requests

WORDS_FILE = "words/words.txt"
DELIMITER = "\n"
URL = 'http://localhost:5000/hash?str='

"""Read the file and thrust word requests to the server to save"""
def main():
    with open(WORDS_FILE, 'r') as words_file:
        for word in words_file.read().split('\n'):
            formatted_url = URL + '{}'.format(word)
            print(formatted_url)
            requests.get(formatted_url)


if __name__=="__main__":
    main()