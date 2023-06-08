import os
import shutil
import csv

# Directory containing fruit images
image_directory = 'path_to_image_directory'

# Path to CSV file containing image labels
csv_file_path = 'path_to_csv_file'

# Output directory for organizing images
output_directory = 'path_to_output_directory'

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read CSV file
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip header row
    for row in reader:
        image_filename = row[0]
        fruit_label = row[1]

        # Path to source image
        source_path = os.path.join(image_directory, image_filename)

        # Path to destination folder
        destination_folder = os.path.join(output_directory, fruit_label)

        # Create destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Path to destination image
        destination_path = os.path.join(destination_folder, image_filename)

        # Move the image to the appropriate folder
        shutil.move(source_path, destination_path)

print('Images have been organized into separate folders based on fruit labels.')
