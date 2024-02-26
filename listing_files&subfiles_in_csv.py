from pathlib import Path
import pandas as pd

root_dir = Path('Folder3')

filepath = root_dir.glob('**/*')

files_list = []
for file in filepath:
    files_list.append(file.name)

df = pd.DataFrame(files_list)
df.to_csv('file.csv')


