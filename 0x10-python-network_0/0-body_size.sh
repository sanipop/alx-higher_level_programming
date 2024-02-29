#!/bin/bash
# A Bash script that takes in a URL, sends a request then displays is body size response 
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
