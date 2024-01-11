import transform
import load
import os

folder_path = r"D:\Kuliah\Kerja Praktik\Data Source"
for folder_name, sub_folders, files in os.walk(folder_path):
    for sub_folder in sub_folders:
        for file in files:
            print(file)
            path = folder_path + '/' + sub_folder + '/' + file
            if sub_folder == "Pasal":
                title, chunks = transform.transform(path)
            else:
                title, chunks = transform.transformNonPasal(path)
            source_id = load.insertSourceMetadata(file, file, title)
            for index, chunk in enumerate(chunks):
                load.insertChunkData(source_id, chunk)