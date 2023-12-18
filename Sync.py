import os
import shutil
import datetime
import argparse

#Replace placeholders like LogFile with the actual paths.
LOG_FILE = "/home/moliveira/Desktop/LogFile.txt"

def sync_folders(source_folder, replica_folder):
    # Make sure the source folder exists
    if not os.path.exists(source_folder):
        log_message("Source folder does not exist.")
        return

    # Get the list of files in the source folder
    source_files = set(os.listdir(source_folder))
    replica_files = set(os.listdir(replica_folder))

    # Synchronize by copying and updating
    for file_name in source_files:
        source_path = os.path.join(source_folder, file_name)
        replica_path = os.path.join(replica_folder, file_name)

        # If the file exists in the replica and is different, update it
        if file_name in replica_files and os.path.getmtime(source_path) != os.path.getmtime(replica_path):
            shutil.copy2(source_path, replica_path)
            log_message(f"Updated: {file_name}")

        # If the file doesn't exist in the replica, copy it
        elif file_name not in replica_files:
            shutil.copy2(source_path, replica_path)
            log_message(f"Copied: {file_name}")

    # Remove files in the replica that don't exist in the source
    for file_name in replica_files - source_files:
        replica_path = os.path.join(replica_folder, file_name)
        os.remove(replica_path)
        log_message(f"Removed: {file_name}")

    log_message("One-way sync complete.")

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"
    with open(LOG_FILE, 'a') as log:
        log.write(log_entry)
        #print in console
        print(log_entry)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform folder synchronization.")
    parser.add_argument("source_folder", help="Path to the source folder.")
    parser.add_argument("replica_folder", help="Path to the replica folder.")
    parser.add_argument("log_file", help="Path to the log file.")

    args = parser.parse_args()

#Replace placeholders like source_folder with the actual paths.
source_folder = "/home/moliveira/Desktop/Source"
replica_folder = "/home/moliveira/Desktop/Replica"


sync_folders(source_folder, replica_folder)
