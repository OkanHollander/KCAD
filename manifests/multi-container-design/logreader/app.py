import time
import glob
import re

LOG_PATH = '/var/logs/*.log'

def tail_files(file_paths, num_entries=5):
    try:
        files = {path: open(path, 'r', encoding='utf-8') for path in file_paths}

        while True:
            for path, file in files.items():
                lines = file.readlines()
                if lines:
                    last_lines = lines[-num_entries:]
                    for line in last_lines:
                        match = re.search(r'New GUID:\s+([0-9a-fA-F-]+)', line)
                        if match:
                            guid = match.group(1)
                            print(guid)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nTailing stopped.")

if __name__ == "__main__":
    log_files = glob.glob(LOG_PATH)

    if not log_files:
        print("No log files found in /app/logs/ directory.")
    else:
        print("Tailing the GUIDs from the following log files:")
        for log_file in log_files:
            print(log_file)
        tail_files(log_files)
