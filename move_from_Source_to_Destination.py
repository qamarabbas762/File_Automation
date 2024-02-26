from pathlib import Path

def move_file(source,destination):
    source_file = source.glob('*')


    for folder in source_file:
        #if folder not in destination:
        new_path = destination / folder.name
        if not new_path.exists():
            folder.rename(new_path)

    print('Mission Successfull')

if __name__ =='__main__':
    source_root_directory = Path('Folder2')
    destination_root_directory = Path('Folder3')

    move_file(source_root_directory,destination_root_directory)


