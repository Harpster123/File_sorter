# File Sorter

A simple Python script that automatically sorts files in a given folder based on their file type.

## Features

- Detects and moves files into subfolders such as:
  - `Images/` (`.jpg`, `.png`, `.gif`, etc.)
  - `Documents/` (`.pdf`, `.docx`, `.txt`, etc.)
  - `Audio/`, `Video/`, `Archives/`
  - `Others/` for everything else
- Uses `Pathlib` and `Shutil` for safe file operations
- Terminal-based: input any folder path

---

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/Harpster123/File_sorter.git
cd File_sorter
