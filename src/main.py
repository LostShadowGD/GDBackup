import os
import shutil
from datetime import datetime

# Define source and destination directories
source_dir = os.path.expanduser("~\\AppData\\Local\\GeometryDash")
backup_root = os.path.expanduser("~\\Documents\\GDBackups")

# Create a backup folder with the current date and time
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_dir = os.path.join(backup_root, current_time)
os.makedirs(backup_dir, exist_ok=True)

# List of files to copy
files_to_copy = [
    "CCGameManager.dat",
    "CCGameManager2.dat",
    "CCLocalLevels.dat",
    "CCLocalLevels2.dat"
]

# Copy each file
for file_name in files_to_copy:
    source_file = os.path.join(source_dir, file_name)
    destination_file = os.path.join(backup_dir, file_name)
    try:
        if os.path.exists(source_file):
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")
        else:
            print(f"File not found: {source_file}")
    except Exception as e:
        print(f"Error copying {file_name}: {e}")

print("Backup process completed.")
