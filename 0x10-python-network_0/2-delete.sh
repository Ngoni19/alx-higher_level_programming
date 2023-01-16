#!/bin/bash
# Send DELETE request, display response body; Use: ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
curl -sX DELETE "$1"
