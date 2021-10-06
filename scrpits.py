from urllib.request import urlopen
import os, hashlib, optparse

def get_remote_md5_sum(url):
  remote = urlopen(url)
  return hash(remote)

def hash(remote, algorithm="md5"):
  max_file_size=100*1024*1024
  hash = hashlib.md5()
  total_read = 0
  while True:
    data = remote.read(4096)
    total_read += 4096
    if not data or total_read > max_file_size:
      break
    hash.update(data)
  return hash.hexdigest()

print(get_remote_md5_sum('https://homologa.cge.mg.gov.br/dataset/082c58f0-8733-43f7-9caf-8b5cf07c3ddf/resource/ce331948-1045-42bb-8afa-4c4042a3badd/download/datapackage.json'))
