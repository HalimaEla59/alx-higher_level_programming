#!/bin/bash
#sends a JSON POST request to URL passed as 1st arg and displays body of response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
