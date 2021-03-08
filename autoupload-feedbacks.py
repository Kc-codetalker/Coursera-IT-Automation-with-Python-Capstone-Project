#!/usr/bin/env python3

import os
import requests

# Describe directory path for feedback data
dir_path = '/data/feedback'

# Load file names
entries = os.listdir(dir_path)

for fname in entries:

  if fname.endswith('.txt'):
    # Define file path
    file_path = os.path.join(os.getcwd(), dir_path, fname)

    try:
      with open(file_path) as f:
        data = f.readlines()
        data_dict = dict()
        data_dict['title'] = data[0]
        data_dict['name'] = data[1]
        data_dict['date'] = data[2]
        data_dict['feedback'] = data[3]

        # Create POST request using created data_dict
        response = requests.post(
          'http://xx.xxx.xxx.xx/feedback/',
          data=data_dict
        )
        print("Returned status code:", response.status_code)
        response.raise_for_status()
        print("Uploaded: " + fname)
    except Exception as e:
      print(e)