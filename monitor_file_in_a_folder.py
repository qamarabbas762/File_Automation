from pathlib import Path
import os
import time

def monitor_file(folder_path,log_file_path):
    old_files = set()

    with open('log_file','a'):
        pass

    while True:
        current_files = set(os.listdir(folder_path))
        new_file = current_files - old_files

        if current_files-old_files:
            log_changes(log_file_path,f"New file added: {', '.join(new_file)})" )
            old_files.update(new_file)

        time.sleep(5)

        deleted_file = old_files-current_files

        if deleted_file:
            log_changes(log_file_path,f"A file got deleted: {', '.join(deleted_file)})")
            old_files-=deleted_file

        time.sleep(5)


def log_changes(log_file_path,message):
    with open(log_file_path,'a') as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        log_file.write(f"[{timestamp}], {message}\n")


if __name__ == "__main__":

    folder_path = Path("Folder5")
    log_file_path = folder_path / Path("log_file.txt")

    monitor_file(folder_path,log_file_path)