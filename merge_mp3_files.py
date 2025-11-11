#!/usr/bin/env python3
import argparse
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(
        description="Merge MP3 files using ffmpeg (concat) and keep cover art from the first file."
    )
    parser.add_argument("directory", help="Directory containing MP3 files")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--sort-by-name", action="store_true", help="Sort files by name")
    group.add_argument("--sort-by-creation-time", action="store_true", help="Sort files by creation time")

    args = parser.parse_args()
    directory = Path(args.directory).resolve()
    output_file = directory.parent / f"{directory.name}.mp3"

    mp3_files = sorted(directory.glob("*.mp3"), key=lambda f: f.name)
    if not mp3_files:
        print(f"No MP3 files found in {directory}")
        return

    if args.sort_by_creation_time:
        mp3_files.sort(key=lambda f: f.stat().st_ctime)
    elif args.sort_by_name:
        mp3_files.sort(key=lambda f: f.name)

    # Create temporary list file
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    list_file = Path(tempfile.gettempdir()) / f"list-{timestamp}.txt"
    with open(list_file, "a") as f:
        for mp3 in mp3_files:
            f.write(f"file '{mp3.resolve()}'\n")

    print(f"Using list file: {list_file}")

    merged_temp = Path(tempfile.gettempdir()) / f"merged-{timestamp}.mp3"

    # Step 1: merge MP3s
    subprocess.run([
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", str(list_file),
        "-c", "copy",
        str(merged_temp)
    ], check=True)

    # Step 2: try to extract cover art from first MP3
    cover_temp = Path(tempfile.gettempdir()) / f"cover-{timestamp}.jpg"
    result = subprocess.run([
        "ffmpeg",
        "-i", str(mp3_files[0]),
        "-an", "-vcodec", "copy", str(cover_temp)
    ], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    if cover_temp.exists() and cover_temp.stat().st_size > 0:
        print("🖼️  Cover art extracted from first MP3")

        # Step 3: embed cover art into merged file
        subprocess.run([
            "ffmpeg",
            "-i", str(merged_temp),
            "-i", str(cover_temp),
            "-map", "0:a",
            "-map", "1:v",
            "-c", "copy",
            "-id3v2_version", "3",
            str(output_file)
        ], check=True)
        cover_temp.unlink(missing_ok=True)
    else:
        print("⚠️  No cover art found in first MP3 — saving merged file without thumbnail")
        merged_temp.rename(output_file)

    # Cleanup
    list_file.unlink(missing_ok=True)
    merged_temp.unlink(missing_ok=True)

    print(f"✅ Merged file saved to: {output_file}")

if __name__ == "__main__":
    main()
