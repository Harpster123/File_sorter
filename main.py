#Filesorter.py
import os
import shutil
from pathlib import Path

from unicodedata import category

#defined file types
EXTENSION_MAP ={
    'Images': ['.jpeg', '.jpg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Audio': ['.mp3', '.wav'],
    'Video': ['.mp4', '.mov'],
    'Archives': ['.zip', '.rar', '.7z'],
}

def get_category(extension):
    for category, ext_list in EXTENSION_MAP.items():
        if extension.lower() in ext_list:
            return category
    return 'Others'

def sort_files(folder_path):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix
            print(f"Detected extension: '{ext}' for file: {file.name}")
            category = get_category(ext)
            target_dir = folder / category
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(target_dir / file.name))
            print(f"Moved {file.name} -> {category}/")

if __name__ == "__main__":
   target = input("Enter folder path to sort:").strip()
   if Path(target).exists():
       sort_files(target)
   else:
       print("Invaild folder path.")

