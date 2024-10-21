import os

def list_files(self, detailed: bool = False):
    try:
        files = os.listdir()
        if not files:
            print("No files in the current directory.")
            return
        if detailed:
            for file in files:
                file_info = os.stat(file)
                print(f"{file} - Size: {file_info.st_size} bytes, Last Modified: {file_info.st_mtime}")
        else:
            for file in files:
                print(file)
    except Exception as e:
        print(f"Error listing files: {e}")
