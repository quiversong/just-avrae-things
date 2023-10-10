#!/usr/local/bin/python3
#!/usr/bin/python3
#!/opt/homebrew/bin/python3
import os
import sys
import re
import logging, sys
import json
import requests
from pathlib import Path

def run(path):
    json_content = read_json(path)
    csv = convert_json_to_csv(json_content)
    print(csv)

def read_json(path):
    content = ''
    with open(path) as f:
        content = f.read()
    return json.loads(content)

def convert_json_to_csv(json_content):
    keys = [x for x in json_content.keys()]
    csv = ''
    for key in keys:
        csv += to_csv_line(key, json_content[key]) + '\n'
    return csv

def to_csv_line(key, json_content):
    line = str(key)[1:]
    for prop in json_content.keys():
        value = json_content[prop]
        if prop == 'loot':
            tokens = value.pop('Foundation Token (1gp)')
            line += f',{tokens}'
            if len(value) == 0:
                line += ','
            else:
                for vk in value.keys():
                    line += f',"""{vk}"": {value[vk]}"'
        elif type(value) == type([]):
            line += ',' + ','.join(f'"{x}"' for x in value)
        else:
            line += f',"{value}"'
    return line

if __name__ == '__main__':
    path = sys.argv[1]
    run(path)
