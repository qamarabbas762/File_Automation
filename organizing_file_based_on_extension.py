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

# from pathlib import Path
#
# root_dir = Path('Folder2')
#
# def make_dir_as_per_the_extension(parent_dir):
#     new_folders = set()  # Using a set to ensure unique folder names
#     for file in parent_dir:
#         if file.is_file():
#             file_ext = file.suffix[1:]  # Extract the extension without the dot
#             new_folders.add(file_ext)
#     return new_folders
#
# def put_the_file_in_new_folders(parent_dir, new_folders):
#     for folder in new_folders:
#         folder_path = root_dir / folder
#         folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
#
#         for file in parent_dir:
#             if file.is_file() and file.suffix[1:] == folder:
#                 new_file_path = folder_path / file.name
#                 file.rename(new_file_path)
#
# def put_files_in_folders(parent_dir, new_folders):
#     for file in parent_dir:
#         if file.is_file():
#             file_ext = file.suffix[1:]
#             folder_path = root_dir / file_ext
#             new_file_path = folder_path / file.name
#             file.rename(new_file_path)
#
#             new_file_path = file.with_name(new_file_name)
#             file.rename(new_file_path)
#
# def main():
#     parent_dir = root_dir.glob('**/*')
#     new_folders = make_dir_as_per_the_extension(parent_dir)
#     put_the_file_in_new_folders(parent_dir, new_folders)
#     put_files_in_folders(parent_dir, new_folders)
#
# if __name__ == "__main__":
#     main()

# from pathlib import Path
#
# def make_dirs_for_extensions(directory):
#     # Get all files in the directory
#     files = directory.glob('*')
#
#     # Extract unique file extensions
#     extensions = set(file.suffix[1:] for file in files if file.is_file())
#
#     # Create a folder for each extension
#     for ext in extensions:
#         (directory / ext).mkdir(exist_ok=True)
#
# def organize_files(directory):
#     # Get all files in the directory
#     files = directory.glob('*')
#
#     # Move each file to the corresponding extension folder
#     for file in files:
#         if file.is_file():
#             ext = file.suffix[1:]
#             new_path = directory / ext / file.name
#             file.rename(new_path)
#
# if __name__ == "__main__":
#     # Specify the directory path
#     root_directory = Path('Folder2')
#
#     # Make directories for each extension
#     make_dirs_for_extensions(root_directory)
#
#     # Organize files into corresponding folders
#     organize_files(root_directory)


from pathlib import Path

def create_extension(directory):
    files = directory.glob('*')

    ext_list = []
    for file in files:
        if file.is_file():
            ext = file.suffix[1:]
            ext_list.append(ext)
    ext_set = set(ext_list)

    for extension in ext_set:
        (directory / extension).mkdir(exist_ok = True)

def organise_file(directory):
    files = directory.glob('*')

    for file in files:
        if file.is_file():
            ext = file.suffix[1:]
            new_path = directory / ext / file.name
            file.rename(new_path)


if __name__ == "__main__":

    root_directory = Path('Folder2')

    create_extension(root_directory)

    organise_file(root_directory)







