#!/usr/bin/env python3
"""
Script for sending PDF report through email.
PDF report are created from description text files.
Generated PDF report would be attached to an email message.
"""

import os
import emails
import reports
from datetime import datetime

def process_data_pdf():
    # Describe directory path for description data
    dir_path = 'supplier-data/descriptions'

    # Load file names
    entries = os.listdir(os.path.join(os.getcwd(), dir_path))

    attachment = '/tmp/processed.pdf'
    title = 'Processed Update on ' + datetime.today().strftime('%Y-%m-%d') + '<br/>'
    paragraph = ''

    for fname in entries:

        if fname.endswith('.txt'):
            # Define file path
            file_path = os.path.join(os.getcwd(), dir_path, fname)

            try:
                with open(file_path) as f:
                    data = f.readlines()
                    paragraph += 'name: ' + data[0] + '<br/>'
                    paragraph += 'weight: ' + data[1] + '<br/>'
                    paragraph += '<br/>'
            except Exception as e:
                print(e)

    return (attachment, title, paragraph)

def main():
    # Generate PDF report to local storage
    attachment, title, paragraph = process_data_pdf()
    reports.generate_report(attachment, title, paragraph)

    # Sending email with PDF report attachment
    sender = 'automation@example.com'
    recipient = 'student-04-6de2bab4fefb@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    email = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(email)

if __name__ == "__main__":
    main()