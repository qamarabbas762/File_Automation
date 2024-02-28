import zipfile
from pathlib import Path

file_location = Path('Folder4')
extract_location = Path('Folder3')

for file in file_location.glob('*.zip'):
    with zipfile.ZipFile(file,'r') as zp:
        destination_file = extract_location / Path('extracted_folder')
        zp.extractall(path=destination_file)
print("Operation complete")

