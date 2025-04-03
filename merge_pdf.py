#!/usr/bin/env python3
"""
A script to merge multiple files into a pdf.
"""

import os 
import subprocess
def main():
    files = []
    output_name = "merged.pdf"
    print(f"Env var is: {os.getenv("NAUTILUS_SCRIPT_SELECTED_FILE_PATHS")}")
    for path in os.getenv("NAUTILUS_SCRIPT_SELECTED_FILE_PATHS",'').splitlines():
        files.append(path);
    magick_command = "magick " + " ".join(files) + " " + output_name
    subprocess.run(["magick"] + files + [output_name])

if __name__ == '__main__':
    main()
