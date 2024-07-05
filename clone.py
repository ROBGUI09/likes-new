import uuid
import os
import shutil

# Original file path
original_file = "python.yml"  # Replace with your actual file name

# Destination directory for cloes
destination_dir = ".github/workflows/"  # You can change this if needed

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Create 100 clones
for i in range(int(input("?: "))):
    # Generate a UUID
    new_filename = f"{uuid.uuid4()}-{os.path.basename(original_file)}"
    new_file_path = os.path.join(destination_dir, new_filename)

    # Copy the original file to the new file path
    shutil.copyfile(original_file, new_file_path)

    print(f"Clone {i+1}: {new_filename} created.")
