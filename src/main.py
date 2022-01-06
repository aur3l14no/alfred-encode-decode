#!/usr/bin/env python3
import json
import urllib.parse
import base64
import sys

s = sys.argv[2]

candidates = []


def try_exec_and_append(l, f):
    try:
        l.append(f())
    except:
        pass


if sys.argv[1] == '-e':
    try_exec_and_append(candidates, lambda: ('base64',
                                             base64.b64encode(s.encode('utf8')).decode('utf8')))
    try_exec_and_append(candidates, lambda: ('urlencode',
                                             urllib.parse.quote_plus(s)))
elif sys.argv[1] == '-d':
    try_exec_and_append(candidates, lambda: ('base64',
                                             base64.b64decode(s.encode('utf8')).decode('utf8')))
    try_exec_and_append(candidates, lambda: ('urldecode',
                                             urllib.parse.unquote_plus(s)))

alfred_results = []

for item in candidates:
    result = {
        "title": item[0],
        "subtitle": item[1],
        "arg": item[1],
        "icon": {
            "path": "./icon.png"
        }
    }
    alfred_results.append(result)

response = json.dumps({
    "items": alfred_results
})

sys.stdout.write(response)
