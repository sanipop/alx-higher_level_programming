#!/usr/bin/python3
"""
Python script input github credentials
and use git Api to display
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(r.json().get('id'))
