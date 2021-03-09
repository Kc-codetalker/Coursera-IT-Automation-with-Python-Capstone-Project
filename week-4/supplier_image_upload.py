#!/usr/bin/env python3

"""
Script to upload images in a directory through a POST API call using requests module.
"""

import os
import requests

# Describe directory path for input and output
dir_path = 'supplier-data/images'
ext = '.jpeg'

# Load file names
entries = os.listdir(os.path.join(os.getcwd(), dir_path))

upload_url = "http://xx.xxx.xxx.xxx/upload/"

for entry in entries:
  # Describe file path for input and output
  entry_path = os.path.join(os.getcwd(), dir_path, entry)

  try:
    if entry_path.endswith(ext):
      with open(entry_path, 'rb') as im:
        r = requests.post(upload_url, files={'file': im})
        print("Uploaded: " + entry_path)
  except Exception as e:
    print(e)

