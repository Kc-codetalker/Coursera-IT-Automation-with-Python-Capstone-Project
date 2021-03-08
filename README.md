# Coursera IT Automation with Python Capstone Project

This is a repository for storing codes I created to finish the capstone project for Coursera IT Automation with Python specialization. Projects are done on `Qwiklabs` with given VM and necessary environment. The project consists of some steps as shown below.

## Step 1: Create Python script to modify images

This step requires a Python script for modifying a set of images using `PIL` library. Input images are stored in a directory and modified images are stored in other directory. Modification includes resizing to 128*128, rotating 90deg anti-clockwise, and converting format to `JPEG (RGB)` from `TIFF`. Script can be read at [fix-icons.py](fix-icons.py).

## Step 2: Create Python script to send data through API call

This step requires a Python script for parsing "feedback" data from text files to an API POST endpoint. Text files are provided inside a directory with the same content format; 4 lines indicating `title`, `name`, `date`, and `feedback`. The script should iterate all files in the directory, create dictionary out of each file, and send them to an API endpoint using `requests` module. Script can be read at [autoupload-feedbacks.py](autoupload-feedbacks.py).

## Step 3: Complete Python script to send PDF file through email

In this step, there are already 5 files provided; 4 Python scripts and a single `car_sales.json` file. [emails.py](./week-3/scripts/emails.py) and [reports.py](./week-3/scripts/reports.py) are pre-completed scripts for managing email requests and generating PDF files respectively. [example.py](./week-3/scripts/example.py) and [cars.py](./week-3/scripts/cars.py) are the ones need to be completed (with TODO description inside).

`example.py` shows example of sending PDF file through email using functions from `emails.py` and `reports.py`. It only requires modifications on some variables as instructed in `Qwiklabs`.

`cars.py` is the real assignment where `process_data(...)` and `main(...)` should be completed (with TODO description inside). `cars.py` would read data from `car_sales.json` and generate a PDF file report from it to be sent through email. The function `process_data(...)` receives the JSON data and generates report summaries to be put inside PDF file. PDF generation and email request are also done using functions from `emails.py` and `reports.py`.

**Notes: I added some #TODO comment myself to help reminding parts I completed myself.