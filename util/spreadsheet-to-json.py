#!/usr/local/bin/python3
#!/usr/bin/python3
import csv
import json
import urllib.request

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRWGInNCIqGDN0YymouN2lLF8uMHsCvq7QZ47Djl_QPJROUJqcQyf5tgSJgPmG6-OQBYvzIr257ZZLO/pub?gid=434315334&single=true&output=csv'

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

text = text.replace('"{', '{').replace('""', '"').replace('},"', '},').replace('"  {', '  {').replace('\r', '').strip()
text = text.split('\n\n')[0]
if text[-1] == ',':
    text = text[0:len(text) - 1]
text = '{"warriors": [\n' + text + '\n]}'

print(text)
