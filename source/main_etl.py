import transform
import load
import os
import json

with open("config.json", 'r') as file:
    sources = json.load(file)

for source in sources:
    folder_path = source["folder_path"]
    split_mode = source["split_mode"]
    unnecessary_patterns = source["unnecessary_patterns"]
    title_patterns = source["title_patterns"]

    for folder_name, sub_folders, files in os.walk(folder_path):
        for file in files:
            path = folder_path + '/' + file

            if split_mode == "page":
                title, chunks = transform.transformNonPasal(path, unnecessary_patterns, title_patterns)
            if split_mode == "pasal":
                title, chunks = transform.transform(path, unnecessary_patterns, title_patterns)

            source_id = load.insertSourceMetadata(file, file, title)

            for index, chunk in enumerate(chunks):
                load.insertChunkData(source_id, chunk)


