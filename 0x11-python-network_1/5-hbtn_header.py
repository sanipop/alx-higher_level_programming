#!/usr/bin/python3
"""inputs url and email
   using request and sys
   displays the value of the variable X-Request-I
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
