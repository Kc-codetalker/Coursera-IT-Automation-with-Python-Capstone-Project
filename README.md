# Coursera IT Automation with Python Capstone Project

This is a repository for storing codes I created to finish the capstone project for Coursera IT Automation with Python specialization. Projects are done on `Qwiklabs` with given VM and necessary environment. The project consists of some assignments as shown below.

## Assignment 1: Create Python script to modify images

This assignment requires a Python script for modifying a set of images using `PIL` library. Input images are stored in a directory and modified images are stored in other directory. Modification includes resizing to 128*128, rotating 90deg anti-clockwise, and converting format to `JPEG (RGB)` from `TIFF`. Script can be read at [fix-icons.py](fix-icons.py).

## Assignment 2: Create Python script to send data through API call

This assignment requires a Python script for parsing "feedback" data from text files to an API POST endpoint. Text files are provided inside a directory with the same content format; 4 lines indicating `title`, `name`, `date`, and `feedback`. The script should iterate all files in the directory, create dictionary out of each file, and send them to an API endpoint using `requests` module. Script can be read at [autoupload-feedbacks.py](autoupload-feedbacks.py).

## Assignment 3: Complete Python script to send PDF file through email

In this assignment, there are already 5 files provided; 4 Python scripts and a single `car_sales.json` file. [emails.py](./week-3/scripts/emails.py) and [reports.py](./week-3/scripts/reports.py) are pre-completed scripts for managing email requests and generating PDF files respectively. [example.py](./week-3/scripts/example.py) and [cars.py](./week-3/scripts/cars.py) are the ones need to be completed (with TODO description inside).

`example.py` shows example of sending PDF file through email using functions from `emails.py` and `reports.py`. It only requires modifications on some variables as instructed in `Qwiklabs`.

`cars.py` is the real assignment where `process_data(...)` and `main(...)` should be completed (with TODO description inside). `cars.py` would read data from `car_sales.json` and generate a PDF file report from it to be sent through email. The function `process_data(...)` receives the JSON data and generates report summaries to be put inside PDF file. PDF generation and email request are also done using functions from `emails.py` and `reports.py`.

**Notes: I added some #TODO comment myself to help reminding parts I completed myself.

## Assignment 4: Wrap up all above
This last assignment integrates all previous scripts on a new use case with slightly different requirements. I basically only reuse all previous scripts and make some adjustments.

The story revolves around uploading supplier images and their respective description to a web server through API call. The images should first be modified into a smaller `JPEG` format. After sending modified images and their description to the web server, an email should be sent to notify the updates on the web server. The tasks are broken down into modifying supplier images, uploading images to a web server, uploading data object to a web server, and sending PDF report through email.

Modifying supplier images is done in [changeImage.py](./week-4/changeImage.py). This script iterates a set of `TIFF` images, performs resizing, then saves them as `JPEG` images. This is basically the same as __Assignment 1__.

Uploading images to a web server is done in [supplier_image_upload.py](./week-4/supplier_image_upload.py). This script iterates a set of `JPEG` images (the ones produced by `changeImage.py`) and send them using `requests` module.

Uploading data object is also similar to uploading images, only differs in data source (using description text files) and utilized API. The script can be read in [run.py](./week-4/run.py), basically the same as __Assignment 2__.

Sending PDF report is done in [report_email.py](./week-4/report_email.py) with the help of [reports.py](./week-4/reports.py) and [emails.py](./week-4/emails.py). I used `reports.py` and `emails.py` from __Assignment 3__ with few modifications to adjust new requirements. `report_email.py` would process description data into a PDF file with `reports.generate_report(...)`, then sending the file as an attachment in an email using `emails.generate_email(...)` and `emails.send_email(...)`.