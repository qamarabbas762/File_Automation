from pathlib import Path

print(Path.cwd())

for path in Path('Folder2').iterdir():
    new_name = 'hello'+path.stem + path.suffix
    print(path.with_name(new_name))
    #path.rename(new_name)

for path in Path('Folder2').iterdir():
    new_name = "hello-" + path.stem +path.suffix
    new_filename = path.with_name(new_name)
    print(new_filename)