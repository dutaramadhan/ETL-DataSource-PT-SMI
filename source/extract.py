import PyPDF2
import os

def extractPDF(filepath):
  pdfReader = PyPDF2.PdfReader(filepath)

  textPDF = ''

  for i in range(len(pdfReader.pages)):
    page = pdfReader.pages[i]
    textPDF += page.extract_text()

  return textPDF