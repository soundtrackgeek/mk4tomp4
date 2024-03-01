import os
import subprocess

# Set the directory where your MP4 files are located
source_directory = '/path/to/your/mp4/files'
# Set the directory where you want to save the MKV files
destination_directory = '/path/to/save/mkv/files'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Loop through all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.mp4'):
        # Construct the full file paths
        source_filepath = os.path.join(source_directory, filename)
        destination_filepath = os.path.join(destination_directory, filename.replace('.mp4', '.mkv'))
        
        # Run the ffmpeg command to convert the file
        subprocess.run(['ffmpeg', '-i', source_filepath, destination_filepath])

print('Conversion complete!')
