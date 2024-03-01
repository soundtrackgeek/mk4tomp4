import os
import subprocess

# Folder containing the .mkv files
folder_path = 'c:\\videos'

# Iterate over all files in the directory
for file_name in os.listdir(folder_path):
    # Check if the file is an .mkv file
    if file_name.endswith('.mkv'):
        # Construct the full file paths
        mkv_file_path = os.path.join(folder_path, file_name)
        mp4_file_name = file_name.replace('.mkv', '.mp4')
        mp4_file_path = os.path.join(folder_path, mp4_file_name)

        # Run the ffmpeg command to convert the file
        subprocess.run(['ffmpeg', '-i', mkv_file_path, '-preset', 'ultrafast', mp4_file_path])

print("Conversion complete.")
