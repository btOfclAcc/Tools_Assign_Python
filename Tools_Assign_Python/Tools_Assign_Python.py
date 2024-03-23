
import urllib.request
import zipfile
import requests
import os
import sys

urls = sys.argv;
urls.pop(0);

for url in urls:
    r = requests.get(url)
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("/", "")
    
    f = open(url + ".txt", "w")
    f.write(r.text)
    f.close()

zp = zipfile.ZipFile('output.zip', mode='w')

for url in urls:
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("/", "")
    zp.write(url + ".txt")

zp.close()

for url in urls:
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("/", "")
    os.remove(url + ".txt")