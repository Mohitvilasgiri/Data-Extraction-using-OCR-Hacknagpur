import os
import requests
import pdfplumber


invoice = 'C:/Users/MOHIT VILAS GIRI/Desktop/Internship 2020/sample.pdf'
invoice_pdf=invoice

with pdfplumber.open(invoice_pdf) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()


file = open("MyFile.txt","w+") 
file.write(text)