#!/bin/bash
#the size
curl -so /dev/null --write-out "%{http_code}" "$1"
