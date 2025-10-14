import os
import random

def rename_files_sequentially(directory):
    """
    Renames all files in the given directory to 1.ext, 2.ext, 3.ext, etc.
    The order is randomized to avoid relying on filesystem order.
    """
    # Get list of files (ignore folders)
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print("⚠️ No files found in the directory.")
        return

    random.shuffle(files)  # Shuffle so order is random

    print(f"📂 Found {len(files)} files. Renaming...")

    # Temporary rename first to avoid overwriting conflicts
    for f in files:
        old_path = os.path.join(directory, f)
        tmp_path = os.path.join(directory, f"temp_{f}")
        os.rename(old_path, tmp_path)

    # Rename to sequential numbers
    temp_files = [f for f in os.listdir(directory) if f.startswith("temp_")]
    for i, f in enumerate(temp_files, start=1):
        old_path = os.path.join(directory, f)
        ext = os.path.splitext(f)[1]  # keep original extension
        new_path = os.path.join(directory, f"{i}{ext}")
        os.rename(old_path, new_path)

    print(f"✅ Done! Renamed {len(temp_files)} files to 1..{len(temp_files)}")

# Example usage:
if __name__ == "__main__":
    target_dir = input("Enter directory path: ").strip()
    rename_files_sequentially(target_dir)
