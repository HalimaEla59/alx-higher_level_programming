#!/bin/bash
#sends request to URL passed as arg and displays only the status code of response.
curl -s -o /dev/null -w "%{http_code}" "$1"
