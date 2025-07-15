import hashlib
import os
import json

HASH_FILE = 'hashes.json'
DIRECTORY_TO_MONITOR = 'files_to_monitor'

def compute_file_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            relative_path = os.path.relpath(filepath, directory)
            file_hashes[relative_path] = compute_file_hash(filepath)
    return file_hashes

def load_previous_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)

def compare_hashes(old_hashes, new_hashes):
    old_files = set(old_hashes.keys())
    new_files = set(new_hashes.keys())

    added_files = new_files - old_files
    deleted_files = old_files - new_files
    modified_files = {f for f in new_files & old_files if old_hashes[f] != new_hashes[f]}

    if not (added_files or deleted_files or modified_files):
        print("✅ No changes detected.")
    else:
        if added_files:
            print("🟩 Added files:")
            for f in added_files:
                print(f"   + {f}")
        if deleted_files:
            print("🟥 Deleted files:")
            for f in deleted_files:
                print(f"   - {f}")
        if modified_files:
            print("🟨 Modified files:")
            for f in modified_files:
                print(f"   * {f}")

def main():
    print(f"🔍 Scanning directory: {DIRECTORY_TO_MONITOR}")
    current_hashes = scan_directory(DIRECTORY_TO_MONITOR)
    previous_hashes = load_previous_hashes()

    compare_hashes(previous_hashes, current_hashes)
    save_hashes(current_hashes)

if __name__ == "__main__":
    main()
