import transform
import load
import os

folderPath = r"D:\Kuliah\Kerja Praktik\Data Source\OneDrive_1_1-4-2024"
for foldername, subfolders, files in os.walk(folderPath):
    for file in files:
        title, chunk = transform.transform(folderPath + '/' + file )