import os
import shutil
from datetime import datetime

def backup_folder(source_folder, backup_folder):

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder_name = f"backup_{timestamp}"
    backup_path = os.path.join(backup_folder, backup_folder_name)
    os.makedirs(backup_path)

    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        backup_subfolder = os.path.join(backup_path, relative_path)

        os.makedirs(backup_subfolder, exist_ok=True)

        for file in files:
            source_file_path = os.path.join(root, file)
            backup_file_path = os.path.join(backup_subfolder, file)
            shutil.copy2(source_file_path, backup_file_path)

    print(f"Backup created successfully at: {backup_path}")