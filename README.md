# FILE-INTEGRITY-CHECKER

 # COMPANY: CODTECH IT SOLUTIONS
 # NAME : Konatham Chennakesavulu
 # INTERN ID : CT06DH1266
 # DOMAIN : CYBER SECURITY AND ETHICAL HACKING
 # DURATION : 6 WEEKS
 # MENTOR : NEELA SANTOSH


# 🛡️ File Integrity Checker

A simple Python tool to monitor changes in files by calculating and comparing SHA-256 hash values. This helps you detect if files have been modified, added, or deleted.

---

## 📦 Features

- ✅ Detects **file modifications**, **new files**, and **deleted files**
- 🧮 Uses secure `SHA-256` hashing
- 📂 Scans entire folder recursively
- 💾 Saves file hashes to `hashes.json` for comparison

---

## 📁 Project Structure

```

file\_integrity\_checker/
├── file\_integrity\_checker.py   # Main script
├── hashes.json                 # Auto-generated: stores known-good hashes
├── files\_to\_monitor/           # Folder to monitor
└── README.md                   # This file

````

---

## 🚀 How It Works

1. On first run, the script scans the `files_to_monitor` directory and stores each file’s SHA-256 hash in `hashes.json`.
2. On subsequent runs, it:
   - Recalculates the current hashes
   - Compares them with the stored hashes
   - Reports any differences (added, deleted, or modified files)

---

## 🛠️ Setup & Installation

### ✅ Requirements
- Python 3.6 or newer

### 📥 Steps

1. **Clone or download** this project.
2. Open a terminal or PowerShell and navigate to the project folder.
3. **Create a folder** called `files_to_monitor` (or use the default one).
4. **Place some files** into the `files_to_monitor` folder.
5. Run the script:

```bash
python file_integrity_checker.py
````

---

## 🧪 Example Output

### No changes:

```
🔍 Scanning directory: files_to_monitor
✅ No changes detected.
```

### After adding a file:

```
🔍 Scanning directory: files_to_monitor
🟩 Added files:
   + new_doc.txt
```

### After deleting a file:

```
🔍 Scanning directory: files_to_monitor
🟥 Deleted files:
   - old_report.pdf
```

### After modifying a file:

```
🔍 Scanning directory: files_to_monitor
🟨 Modified files:
   * notes.md
```

---

## 🔧 Customization

You can change these in the script:

```python
HASH_FILE = 'hashes.json'                 # File to store hash data
DIRECTORY_TO_MONITOR = 'files_to_monitor' # Directory to monitor
```

---

## 📌 To Reset the Baseline

Delete the `hashes.json` file:

```bash
rm hashes.json
```

Then rerun the script to generate a new baseline.

---

## 📚 Future Enhancements (optional ideas)

* CLI interface with `argparse`
* File size or timestamp reporting
* Scheduling with Task Scheduler or `cron`
* Email alerts when changes are detected
* GUI frontend using Tkinter or PyQt

---

## 📝 License

MIT License — free to use, modify, and share.



## OUTPUT:
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/ed715f1c-e5b8-4077-9c6b-db10cd612316" />
