from pathlib import Path

p1 = Path(r'C:\Users\Ashu\PycharmProjects\file_automation\Folder2')

for i in p1.iterdir():
    print(i.suffix)
print('\n\n')

for i in p1.iterdir():
    print(i.stem)

print('\n\n')

for i in p1.iterdir():
    print(i.name)
# from pathlib import Path
#
# # Provide the path to the directory
# directory_path = r'C:\Users\Ashu\PycharmProjects\file_automation\Folder2'
#
# # Use Path to create a Path object for the directory
# directory_path_obj = Path(directory_path)
#
# # Iterate over the files in the directory
# for file_path in directory_path_obj.iterdir():
#     print(file_path.suffix)
