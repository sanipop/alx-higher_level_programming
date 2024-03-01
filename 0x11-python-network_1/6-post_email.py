#!/usr/bin/python3
"""
Inputs url and emails,
send the post request
and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
