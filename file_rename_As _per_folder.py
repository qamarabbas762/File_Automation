# from pathlib import Path
#
# root_dir = Path('Folder2')
#
# filepath = root_dir.glob("**/*")
#
# for file in filepath:
#     if file.is_file():
#         parent_folder = file.parts[-2]
#         new_file_name = parent_folder+'-'+file.name
#         new_file_path = file.with_name(new_file_name)
#         file.rename(new_file_path)

from pathlib import Path

root_dir = Path('Folder2')

filepath = root_dir.glob('**/*')

for file in filepath:
    if file.is_file():
        parent_name = file.parts[-2]
        new_file_name = parent_name+'-'+file.name
        new_file_path = file.with_name(new_file_name)
        file.rename(new_file_path)

        

