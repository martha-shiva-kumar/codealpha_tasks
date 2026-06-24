# Task 3: Task Automation with Python Scripts

A Python script to automate moving `.jpg` and `.jpeg` files from one folder to another for my CodeAlpha internship.

## Features
- User inputs source and destination folder paths
- Validates if source folder exists
- Creates destination folder if it doesn't exist
- Moves all `.jpg` and `.jpeg` files (case-insensitive)
- Shows summary of moved files
- Handles errors gracefully

## How to Run
```bash
python automation.py
```

## Sample Output
```
Enter source folder path: C:\Users\shiva\Desktop\SourceFolder
Enter destination folder path: C:\Users\shiva\Desktop\DestFolder
Destination folder exists: C:\Users\shiva\Desktop\DestFolder
Moved: photo.jpg
Moved: image.jpeg

Successfully moved 2 file(s)!
```

## Technologies Used
- `os` — folder and file operations (`os.path.exists`, `os.listdir`, `os.makedirs`, `os.path.join`)
- `shutil` — move files (`shutil.move`)
- Input validation
- File handling
- String methods (`.lower()`, `.endswith()`)

## Internship
- **Company:** CodeAlpha
- **Duration:** 20th June 2026 - 20th July 2026
- **Domain:** Python Programming
