#!/usr/local/bin/python3
#!/usr/bin/python3
import csv
import json
import urllib.request
import sys


# Duel Data
# url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRWGInNCIqGDN0YymouN2lLF8uMHsCvq7QZ47Djl_QPJROUJqcQyf5tgSJgPmG6-OQBYvzIr257ZZLO/pub?gid=434315334&single=true&output=csv'

# Road Data
# https://docs.google.com/spreadsheets/d/1mRV2AeFauXfzQIVAb0kE1DCZapWWQQ3l1kJr3Ov-q80/pub?gid=0&single=true&output=csv
key = sys.argv[1]
url = sys.argv[2]

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

text = text.replace('"{', '{').replace('""', '"').replace('},"', '},').replace('"  {', '  {').replace('\r', '').strip()
text = text.split('\n\n')[0]
if text[-1] == ',':
    text = text[0:len(text) - 1]
text = '{"' + key + '": [\n' + text + '\n]}'

print(text)
