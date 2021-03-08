# Coursera IT Automation with Python Capstone Project
===

This is a repository for storing codes I created to finish the capstone project for Coursera IT Automation with Python specialization. The project consists of some steps as shown below.

## Step 1: Create Python script to modify images

This step requires a Python script for modifying a set of images using __PIL__ library. Input images are stored in a directory and modified images are stored in other directory. Modification includes resizing to 128*128, rotating 90deg anti-clockwise, and converting format to JPEG (RGB) from TIFF. Script can be read at [fix-icons.py](fix-icons.py).

## Step 2: Create Python script to send data through API call

This step requires a Python script for parsing "feedback" data from text files to an API POST endpoint. Text files are provided inside a directory with the same content format; 4 lines indicating "title", "name", "date", and "feedback". The script should iterate all files in the directory, create dictionary out of each file, and send them to an API endpoint using __requests__ module. Script can be read at [autoupload-feedbacks.py](autoupload-feedbacks.py).