# file-integrity-monitor

## Description
A Python script to monitor a file's integrity by calculating and comparing its SHA-256 hash periodically. The script alerts the user if the file's content changes, indicating potential tampering or corruption.

## Features
- Calculates the SHA-256 hash of the specified file.
- Periodically checks for any changes in the file's content.
- Alerts the user if the file's integrity is compromised.

## Prerequisites
- Python 3.x installed.
- Basic knowledge of file paths and system navigation.

## How to Use
1. Save the script to a file (e.g., `integrity_monitor.py`).
2. Open your terminal or command prompt.
3. Run the script using:
   ```bash
   python integrity_monitor.py
