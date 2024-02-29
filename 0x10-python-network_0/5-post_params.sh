#!/bin/bash
# use curl send email witha given SUBJECT
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
