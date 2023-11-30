#!/bin/bash
#takes URL as arg, sends GET request to URL, displays the doby of the responce
curl -sX GET -H "X-School-User-Id: 98" "$1"
