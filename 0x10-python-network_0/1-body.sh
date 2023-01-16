#!/bin/bash
# GET request to URL, display body of a 200 response; Run websever: ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
curl -sL "$1"
