import shutil
import os

def upload_to_drive(local_path, drive_path="/content/drive/MyDrive/FortiCryptX-Uploads"):
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"{local_path} not found.")

    os.makedirs(drive_path, exist_ok=True)
    filename = os.path.basename(local_path)
    destination = os.path.join(drive_path, filename)
    shutil.copy2(local_path, destination)
    print(f"Uploaded: {filename} to Google Drive -> {drive_path}")

def download_from_drive(drive_filename, drive_path="/content/drive/MyDrive/FortiCryptX-Uploads", download_dir="/content"):
    source_path = os.path.join(drive_path, drive_filename)
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"{drive_filename} not found in Drive folder.")

    destination = os.path.join(download_dir, drive_filename)
    shutil.copy2(source_path, destination)
    print(f"Downloaded: {drive_filename} to {download_dir}")
    return destination
