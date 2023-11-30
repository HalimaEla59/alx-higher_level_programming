#!/bin/bash
#sends DELETE request to URL passed as first arg, displays body of response
curl -sX DELETE "$1"
