# from pathlib import Path
#
# def move_file(source,destination):
#     source_file = source.glob('*')
#
#
#     for folder in source_file:
#         #if folder not in destination:
#
#         new_path = destination / folder.name
#         old_path = source / folder.name
#         if not new_path.exists():
#             folder.rename(new_path)
#             # folder.rename(old_path)
#         folder.rename(old_path)
#
#     print('Mission Successfull')
#
# if __name__ =='__main__':
#     source_root_directory = Path('Folder2')
#     destination_root_directory = Path('Folder3')
#
#     move_file(source_root_directory,destination_root_directory)










# from pathlib import Path
#
# path = Path('Folder2')
# path2 = Path('Folder3')
#
# files = path.glob('**/*')
#
# #file2 = path.glob('**/*')
#
# for file in path2.iterdir():
#     new_path = path2 / file
#
#     print(new_path)



