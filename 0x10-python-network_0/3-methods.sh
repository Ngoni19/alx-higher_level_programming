#!/bin/bash
#Display all methods accepted; Use ./3-methods.sh 0.0.0.0:5000/route_4
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
