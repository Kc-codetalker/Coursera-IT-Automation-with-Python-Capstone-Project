#!/usr/bin/env python3

"""
Provide function to generate simple PDF file.
"""

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, body):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(body, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])
