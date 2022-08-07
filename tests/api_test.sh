#!/bin/bash

curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/checkout -d '["001", "002", "001", "004", "003"]'
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/checkout -d '["001", "002", "001", "004", "999"]'
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/checkout1 -d '["001", "002", "001", "004"]'
curl -X GET http://127.0.0.1:5000/checkout
