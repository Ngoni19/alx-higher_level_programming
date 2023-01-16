#!/bin/bash
#Display status code only; Use: ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
curl -o /dev/null -w '%{http_code}' -sL "$1"
