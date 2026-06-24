import os
import shutil

# Step 1: Get source and destination from user
source = input("Enter source folder path: ").strip()
destination = input("Enter destination folder path: ").strip()

# Step 2: Check if source folder exists
if not os.path.exists(source):
    print("Error: Source folder does not exist!")
    exit()

# Step 3: Create destination folder if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)
    print(f"Created destination folder: {destination}")
else:
    print(f"Destination folder exists: {destination}")

# Step 4: Loop through files and move .jpg/.jpeg
moved_count = 0

for filename in os.listdir(source):
    # Check if file ends with .jpg or .jpeg (case-insensitive)
    if filename.lower().endswith(('.jpg', '.jpeg')):
        # Build full paths
        src_path = os.path.join(source, filename)
        dst_path = os.path.join(destination, filename)
        
        # Move the file
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename}")
        moved_count += 1

# Step 5: Print summary
if moved_count > 0:
    print(f"\nSuccessfully moved {moved_count} file(s)!")
else:
    print("\nNo .jpg or .jpeg files found in source folder.")