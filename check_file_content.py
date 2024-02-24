import os

def are_files_equal(file_path1, file_path2):
    with open(file_path1, 'rb') as file1, open(file_path2, 'rb') as file2:
        return file1.read() == file2.read()

def find_and_remove_duplicates(directory):
    files = []

    # Collect all file paths
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    # Compare each file with every other file
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = files[i]
            file2 = files[j]

            if os.path.exists(file1) and os.path.exists(file2) and are_files_equal(file1, file2):
                # Duplicate file found, remove it
                print(f"Duplicate found: {file1} and {file2}")
                os.remove(file2)

# if __name__ == "__main__":
directory_path = "/path/"
find_and_remove_duplicates(directory_path)
