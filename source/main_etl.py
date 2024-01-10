import transform
import load
import os

folder_path = r"D:\Kuliah\Kerja Praktik\Data Source\OneDrive_1_1-4-2024"
for folder_name, sub_folders, files in os.walk(folder_path):
    for file in files:
        print(file)
        path = folder_path + '/' + file
        title, chunks = transform.transform(path)
        source_id = load.insertSourceMetadata(file, file, title)
        for index, chunk in enumerate(chunks):
            load.insertChunkData(source_id, chunk)