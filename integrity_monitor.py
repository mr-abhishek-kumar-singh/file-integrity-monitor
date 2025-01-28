import hashlib
import time

def calculate_hash(file_path):
    """
    Calculates the SHA-256 hash of a given file.

    Args:
        file_path (str): Path to the file to be hashed.

    Returns:
        str: SHA-256 hash as a hexadecimal string.
    """
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            return hashlib.sha256(content).hexdigest()  # Convert binary to readable hexadecimal string
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None

def monitor_file(file_path, interval=5):
    """
    Monitors the file for any integrity changes based on its SHA-256 hash.

    Args:
        file_path (str): Path to the file to be monitored.
        interval (int): Time interval (in seconds) between integrity checks.
    """
    original_hash = calculate_hash(file_path)
    if original_hash is None:
        return

    print(f"Monitoring integrity of '{file_path}'...")
    while True:
        current_hash = calculate_hash(file_path)
        if current_hash is None:
            break
        if current_hash != original_hash:
            print("[!] File integrity compromised!")
            break
        time.sleep(interval)

# Get user input for file path and monitoring interval
file_path = input("Enter the path to the file to monitor: ")
try:
    interval = int(input("Enter the monitoring interval in seconds (default: 5): ") or 5)
    if interval <= 0:
        raise ValueError("Interval must be a positive integer.")
    monitor_file(file_path, interval)
except ValueError as e:
    print(f"Error: {e}")
