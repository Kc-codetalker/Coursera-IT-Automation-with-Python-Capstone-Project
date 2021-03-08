#!/usr/bin/env python3

import os
from PIL import Image

in_path = 'images'
out_path = '/opt/icons'
ext = '.jpeg'
entries = os.listdir(in_path)

try:
  os.makedirs(os.path.join(os.getcwd(), out_path))
except Exception as e:
  print(e)

for entry in entries:
  entry_path = os.path.join(os.getcwd(), in_path, entry)
  save_path = os.path.join(out_path, entry+ext)

  try:
    im = Image.open(entry_path)
    new_im = im.resize((128,128)).rotate(90).convert("RGB")
    new_im.save(save_path, "JPEG")
  except Exception as e:
    print(e)

  print("Processed: " + entry_path)
