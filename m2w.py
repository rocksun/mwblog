import requests
import sys
import os
import base64
import json

username = 'rocksun'
password = os.environ.get("WP_PASSWORD")
creds = username + ':' + password
cred_token = base64.b64encode(creds.encode())

header = {
    'Authorization': 'Basic ' + cred_token.decode('utf-8'),
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    }

baseSrc = 'https://github.com/rocksun/mwblog/blob/master'

if len(sys.argv) != 2:
    print("please provide a markdown file")
    sys.exit(1)

file_name = sys.argv[1]
slug = os.path.basename(file_name).replace(".md","")
abs_file_path = os.path.abspath(file_name)

relative_file_path = abs_file_path.split('mwblog')[1].replace("\\","/")
target_path = baseSrc + relative_file_path
print("target: ", target_path)

with open(file_name, encoding="utf-8") as f:
    lines = f.readlines()

meta_data = {}
for line in lines:
    line = line.strip()
    if line.startswith('<!--'):
        continue
    elif line.startswith('-->'):
        break
    else:
        keyvalues = line.split(':', 1)
        if len(keyvalues) == 2:
            meta_data[keyvalues[0].strip()] = keyvalues[1].strip()

title = meta_data['title']
content = '[git-github-markdown url="'+target_path+'"]'

data = {
  'title': title,
  'slug': slug,
  'content': content,
  'status': 'draft',
#   'tags': meta_data['keywords'].split(','),
#   'featured_media': meta_data['cover'],
}

print(data)

endpoint = 'https://yylives.cc/wp-json/wp/v2/posts'

response = requests.post(endpoint, headers=header, json=data, verify=False)

print(response.status_code)
print(response.text)