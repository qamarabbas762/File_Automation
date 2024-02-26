# from pathlib import Path
#
# root_dir = Path('Folder2')
#
# parent_dir = root_dir.glob('**/*')
#
#
#
# def make_dir_asper_the_extension(parent_dir = parent_dir):
#     new_folders = []
#     for file in parent_dir:
#
#
#         if file.is_file():
#             file_ext = file.suffix
#             new_folders.append(file_ext[1:])
#     return new_folders
#
#
# def put_the_file_in_new_folders(parent_dir=parent_dir):
#     folder = make_dir_asper_the_extension()
#     for i in folder:
#         for file in parent_dir:
#             if file.suffix == i:
#                 file.mkdir(folder)

from pathlib import Path

root_dir = Path('Folder2')

def make_dir_as_per_the_extension(parent_dir):
    new_folders = set()  # Using a set to ensure unique folder names
    for file in parent_dir:
        if file.is_file():
            file_ext = file.suffix[1:]  # Extract the extension without the dot
            new_folders.add(file_ext)
    return new_folders

def put_the_file_in_new_folders(parent_dir, new_folders):
    for folder in new_folders:
        folder_path = root_dir / folder
        folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist

        for file in parent_dir:
            if file.is_file() and file.suffix[1:] == folder:
                new_file_path = folder_path / file.name
                file.rename(new_file_path)

def put_files_in_folders(parent_dir, new_folders):
    for file in parent_dir:
        if file.is_file():
            file_ext = file.suffix[1:]
            folder_path = root_dir / file_ext
            new_file_path = folder_path / file.name
            file.rename(new_file_path)

            new_file_path = file.with_name(new_file_name)
            file.rename(new_file_path)

def main():
    parent_dir = root_dir.glob('**/*')
    new_folders = make_dir_as_per_the_extension(parent_dir)
    put_the_file_in_new_folders(parent_dir, new_folders)
    put_files_in_folders(parent_dir, new_folders)

if __name__ == "__main__":
    main()









