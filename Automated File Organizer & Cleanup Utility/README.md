# Automated File Organizer & Cleanup Utility

A lightweight Python utility that automatically organizes files in a selected directory into categorized folders based on their file extensions. It helps reduce directory clutter, improves file accessibility, and handles common file-management errors.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Categories](#file-categories)
- [Testing](#testing)
- [Logging](#logging)
- [Error Handling and Safety](#error-handling-and-safety)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

Directories such as Downloads often accumulate documents, images, videos, archives, and source code files. Finding specific files in these directories can become difficult over time.

The Automated File Organizer & Cleanup Utility automates this process by identifying file extensions and moving files into appropriate category folders.

The application supports a dry-run mode to preview proposed changes before moving files.

## Features

- **Automatic file categorization:** Organizes files according to their extensions.
- **Dynamic folder creation:** Creates category folders when required.
- **Dry-run mode:** Previews file movements without modifying files.
- **Duplicate filename handling:** Generates alternative filenames to help prevent overwriting existing files.
- **Error handling:** Handles common filesystem and permission errors.
- **Execution summary:** Displays the number of processed, skipped, and failed files.
- **Logging:** Records execution details in a log file.
- **Unknown file support:** Places unsupported file extensions in an `Others` folder.
- **Command-line interface:** Allows users to organize directories through terminal commands.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `os` | Directory scanning |
| `shutil` | Moving files |
| `pathlib` | Cross-platform path handling |
| `argparse` | Command-line argument handling |
| `logging` | Execution and error logging |
| `unittest` | Automated testing |
| PowerShell | Running commands on Windows |

## Project Structure

```text
Automated-File-Organizer/
│
├── organizer.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── logs/
│   └── organizer.log
│
├── test_files/
│   ├── Documents/
│   ├── Images/
│   ├── Videos/
│   ├── Archives/
│   ├── Code/
│   └── Others/
│
└── tests/
    └── test_organizer.py
```

The category folders inside `test_files/` are generated during execution. Your initial test directory may contain individual sample files instead.

## Requirements

- Python 3.10 or later recommended.
- Windows, macOS, or Linux.
- A terminal or command prompt.
- No third-party Python packages are required for the current implementation.

## Installation

### 1. Clone the repository

If the project has already been uploaded to GitHub:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Verify Python installation

On Windows, open PowerShell and run:

```powershell
py --version
```

On macOS or Linux, run:

```bash
python3 --version
```

If Python is not installed, download it from the official website:

https://www.python.org/downloads/

On Windows, enable the option to add Python to PATH during installation if available.

### 3. Create a virtual environment (optional)

On Windows:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

A virtual environment is optional because this project currently uses only Python's standard library.

### 4. Install dependencies

The project does not require external dependencies.

You can keep `requirements.txt` with the following content:

```text
# No external dependencies required.
```

No `pip install` command is necessary.

## Usage

Run the following commands from the project root directory.

### 1. Preview file organization

On Windows:

```powershell
py organizer.py test_files
```

On macOS or Linux:

```bash
python3 organizer.py test_files
```

By default, the program runs in dry-run mode. It displays the proposed file movements without actually moving the files.

### 2. Organize files

On Windows:

```powershell
py organizer.py test_files --apply
```

On macOS or Linux:

```bash
python3 organizer.py test_files --apply
```

The `--apply` flag enables actual file movement.

### 3. Organize a specific directory

For example, to organize your Downloads directory on Windows:

```powershell
py organizer.py "$HOME\Downloads"
```

Review the preview, then execute:

```powershell
py organizer.py "$HOME\Downloads" --apply
```

**Important:** Always review the dry-run output before organizing an important directory.

### 4. View the resulting directory structure

On Windows:

```powershell
tree test_files /F
```

On macOS or Linux:

```bash
find test_files -maxdepth 2 -print
```

## File Categories

The organizer uses a predefined extension mapping to determine the destination folder.

| Category | Example extensions |
|---|---|
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.svg` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Code | `.py`, `.java`, `.js`, `.html`, `.css`, `.cpp`, `.c`, `.json`, `.sql` |
| Others | File extensions not included in the mapping |

Additional extensions can be supported by updating the `EXTENSION_MAP` dictionary in `organizer.py`.

## Testing

The project includes unit tests for extension mapping, duplicate filename handling, and unknown extensions.

Run the tests from the project root:

```powershell
py -m unittest discover -s tests -v
```

On macOS or Linux:

```bash
python3 -m unittest discover -s tests -v
```

Review the test output to confirm whether the tests pass.

## Logging

The application records execution information in:

```text
logs/organizer.log
```

On Windows, display the latest log entries using:

```powershell
Get-Content logs\organizer.log -Tail 20
```

Logs can help identify permission problems and file movement errors.

## Error Handling and Safety

- The program handles common permission and filesystem errors.
- Duplicate destination filenames are assigned alternative names where possible.
- Symbolic links are excluded from the top-level file scan.
- The default dry-run mode does not move files.
- Existing category folders are reused rather than recreated.
- Files are moved only from the selected directory's top level; subdirectories are not scanned recursively.

**Note:** The organizer does not guarantee protection against every filesystem race condition or storage failure. Review important files and maintain backups before running bulk operations.

## Limitations

- File classification is based on extensions rather than file contents.
- The program does not recursively organize nested directories.
- No graphical user interface is included in the current version.
- There is no automatic undo or restoration feature.
- File movements may fail if the destination is inaccessible or the source is in use.

## Future Enhancements

Potential improvements include:

- A graphical interface using Tkinter.
- Recursive directory organization.
- Duplicate file detection using file hashes.
- Empty-folder detection and cleanup.
- Undo functionality for completed operations.
- Configurable extension mappings.
- Scheduled automatic organization.
- Detailed timestamped reports and improved logging.

## License

This project is available for educational and personal use. If you plan to publish it as an open-source project, consider adding a `LICENSE` file with your chosen license, such as the MIT License.

---

**Project:** Automated File Organizer & Cleanup Utility  
**Language:** Python  
**Project Type:** Desktop Automation  
**Status:** Core file organization functionality implemented
