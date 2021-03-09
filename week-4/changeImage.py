#!/usr/bin/env python3

"""
Script to modify images in a directory and save them back.
Modifications include resizing and extension conversion.
"""

import os
from PIL import Image

def change_ext(fname, old_ext, new_ext):
    if fname.endswith(old_ext):
        idx = fname.rfind(old_ext)
        return fname[:idx] + new_ext
    return fname

# Describe directory path for input and output
dir_path = 'supplier-data/images'
old_ext = '.tiff'
new_ext = '.jpeg'

# Load file names
entries = os.listdir(os.path.join(os.getcwd(), dir_path))

for entry in entries:
  # Describe file path for input and output
  entry_path = os.path.join(os.getcwd(), dir_path, entry)
  new_entry = change_ext(entry, old_ext, new_ext)
  save_path = os.path.join(os.getcwd(), dir_path, new_entry)

  try:
    im = Image.open(entry_path)
    new_im = im.convert("RGB").resize((600,400))
    new_im.save(save_path, "JPEG")
  except Exception as e:
    print(e)

  print("Processed: " + entry_path)
