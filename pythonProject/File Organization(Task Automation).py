import os
import shutil

# Define the directory to organize
directory = 'path/to/your/directory'

# Define the subfolders for different file types
file_types = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.rar']
}

# Create the subfolders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move the files to their respective subfolders
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1]
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                break

print("Files have been organized successfully!")



# Steps to Use the Script:
# Replace 'path/to/your/directory' with the path to the directory you want to organize.

# Add or modify the file extensions in the file_types dictionary as needed.

# Save the script to a .py file and run it using a Python interpreter.
