import PyPDF2
import os

def extractPDF(filepath):
  pdf_reader = PyPDF2.PdfReader(filepath)

  textpdf = ''

  for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    textpdf += page.extract_text()

  return textpdf