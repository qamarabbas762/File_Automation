from pathlib import Path
path = Path('Folder4')

files = path.glob('*')

for file in files:
    new_file_path = file.with_suffix('.txt')
    file.rename(new_file_path)