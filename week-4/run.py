#! /usr/bin/env python3

"""
Script to upload data in a set of files through a POST API call using requests module.
Data are stored in individual text files with each lines represent an attribute.
The script would read each file and create Python dictionary out of them.
This dictionary would then be sent using API call as data.
"""

import os
import requests

# Describe directory path for description data
dir_path = 'supplier-data/descriptions'

# Load file names
entries = os.listdir(os.path.join(os.getcwd(), dir_path))

for fname in entries:

  if fname.endswith('.txt'):
    # Define file path
    file_path = os.path.join(os.getcwd(), dir_path, fname)

    try:
      with open(file_path) as f:
        data = f.readlines()
        data_dict = dict()
        data_dict['name'] = data[0]
        data_dict['weight'] = int(data[1].split()[0])
        data_dict['description'] = data[2]
        data_dict['image_name'] = fname[:fname.rfind('.txt')] + '.jpeg'

        # Create POST request using created data_dict
        response = requests.post(
          'http://xx.xx.xxx.xxx/fruits/',
          data=data_dict
        )
        print("Returned status code:", response.status_code)
        response.raise_for_status()
        print("Uploaded: " + fname)
    except Exception as e:
      print(e)