import transform
import load
import os

folderPath = r"D:\Kuliah\Kerja Praktik\Data Source\OneDrive_1_1-4-2024"
for foldername, subfolders, files in os.walk(folderPath):
    for file in files:
        path = folderPath + '/' + file
        title, chunks = transform.transform(path)
        source_id = load.insertSourceMetadata(file, file, title)
        for chunk in chunks:
            load.insertChunkData(source_id, chunk)