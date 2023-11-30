#!/bin/bash
# Bash script takes a URL, sends the URL Content-Length from HTTP request
curl -sI "$1" | wc -c
