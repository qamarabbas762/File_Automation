import zipfile
from pathlib import Path

search_folder = Path('Folder3')

for file in search_folder.glob("**/*"):
    if 'New' in file.stem:
        print(file)