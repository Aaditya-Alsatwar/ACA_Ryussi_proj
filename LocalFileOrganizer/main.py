import os
import shutil
import mimetypes

def organize_files(directory):
    # Define categories and their associated folder names
    categories = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Others': []  # Files that don't match any category
    }
    
    # Create folders if they don't exist
    for folder in categories.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine file type and move to appropriate folder
        file_ext = os.path.splitext(file)[1].lower()
        moved = False
        
        for category, extensions in categories.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(directory, category, file))
                moved = True
                break
        
        # If no category matches, move to 'Others'
        if not moved:
            shutil.move(file_path, os.path.join(directory, 'Others', file))

    print("Files organized successfully!")

# Specify the directory to organize
target_directory = input("Enter the directory path to organize: ").strip()
if os.path.isdir(target_directory):
    organize_files(target_directory)
else:
    print("Invalid directory path.")
