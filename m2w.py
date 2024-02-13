import requests
import sys
import os
import base64
import json
import webbrowser 

def get_image_name(img_url):
    last_slash_idx = img_url.rfind('/')
    if last_slash_idx == -1:
        return img_url
    filename_with_ext = img_url[last_slash_idx+1:]
    return filename_with_ext

def download_image(url, path):
    if not os.path.exists(path):
        os.makedirs(path)

    targetImage = os.path.join(path, get_image_name(url))

    if not os.path.exists(targetImage):
        with open(targetImage, "wb") as f:
            response = requests.get(url)
            f.write(response.content)
    else:
        print("file already downloaded")

    return targetImage




username = 'rocksun'
password = os.environ.get("WP_PASSWORD")
creds = username + ':' + password
cred_token = base64.b64encode(creds.encode())

header = {
    'Authorization': 'Basic ' + cred_token.decode('utf-8'),
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    }

baseSrc = 'https://github.com/rocksun/mwblog/blob/master'
baseEndPoint = 'https://yylives.cc/wp-json/wp/v2/'

def upload_image(image_path):
    files = {'file': open(image_path, 'rb')}
    r = requests.post(baseEndPoint + 'media', headers=header, files=files, verify=False)
    print(r)
    return r.json()['id']



if len(sys.argv) != 2:
    print("please provide a markdown file")
    sys.exit(1)

file_name = sys.argv[1]
slug = os.path.basename(file_name).replace(".md","")
abs_file_path = os.path.abspath(file_name)
directory = os.path.dirname(abs_file_path)

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
content = '[git-github-markdown url="'+target_path+'" cache_ttl="3600"]'

data = {
  'title': title,
  'slug': slug,
  'content': content,
  'status': 'draft',
#   'tags': meta_data['keywords'].split(','),
#   'featured_media': meta_data['cover'],
}

print(data)

print("download cover images")
targetImage = download_image(meta_data['cover'], directory)
print("upload cover images")
imageID = upload_image(targetImage)
print("Media ID: ", imageID)

data['featured_media'] = imageID


endpoint = baseEndPoint+'posts'

response = requests.post(endpoint, headers=header, json=data, verify=False)

print(response.status_code)

if response.status_code == 201:
    post_id = response.json()["id"]
    url = "https://yylives.cc/wp-admin/post.php?post=%s&action=edit" % post_id
    webbrowser.open(url)