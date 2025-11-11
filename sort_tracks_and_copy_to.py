#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
from pathlib import Path
import eyed3
#TODO: add a comment of the command to use to check that track numbers have been set properly.

def get_sorted_files(src_dir):
    """Get files sorted by birth time using stat %W"""
    try:
        # os.stat() does not support birth time for some reason
        stat_output = subprocess.check_output(
            ['find', src_dir, '-maxdepth', '1', '-type', 'f', '-exec', 
             'stat', '--printf=%W\\t%n\\0', '{}', '+'],
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        return []

    files = []
    entries = stat_output.split(b'\0')[:-1]
    for entry in entries:
        timestamp_str, path = entry.split(b'\t', 1)
        timestamp = int(timestamp_str) if timestamp_str.isdigit() else 0
        if timestamp <= 0:
            timestamp = os.path.getmtime(path.decode())
        files.append((timestamp, path.decode()))

    return [fp for (ts, fp) in sorted(files, key=lambda x: x[0])]

def update_id3_tags(path, track_num):
    """Update tags without destroying album art"""
    try:
        audiofile = eyed3.load(path)
        if audiofile.tag:
            audiofile.tag.track_num = track_num
            audiofile.tag.save(version=eyed3.id3.ID3_V2_4)
            return True
    except Exception as e:
        print(f"Tag error: {e}")
    return False

def process_source(source_dir, target_root):
    """Process a single source directory"""
    src = Path(source_dir).expanduser().resolve()
    if not src.is_dir():
        print(f"Skipping invalid source: {source_dir}")
        return 0

    dest = target_root / src.name
    try:
        dest.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print(f"Skipping {src.name} - destination exists")
        return 0

    sorted_files = get_sorted_files(str(src))
    if not sorted_files:
        print(f"No files found in {src.name}")
        return 0

    copied_files = []
    for idx, src_path in enumerate(sorted_files, 1):
        src_path = Path(src_path)
        dest_name = f"T{idx:03d}-{src_path.name}"
        dest_path = dest / dest_name
        shutil.copy2(src_path, dest_path)
        copied_files.append(dest_path)
        print(f"Copied: {dest.name}/{dest_name}")

    print(f"\nUpdating metadata in {src.name}:")
    success_count = 0
    for track_num, mp3_path in enumerate(copied_files, 1):
        if mp3_path.suffix.lower() == '.mp3':
            if update_id3_tags(mp3_path, track_num):
                print(f"  ✓ Track {track_num}: {mp3_path.name}")
                success_count += 1
            else:
                print(f"  ✗ Failed: {mp3_path.name}")

    print(f"Processed {len(sorted_files)} files ({success_count} MP3s updated)")
    return len(sorted_files)

def main():
    # using yt-dlp you can download the playlists programmatically
    # and then extract the albums properly
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <source_dir1> [source_dir2...] <target_dir>")
        print(f"Example: python3 ./sort_tracks_and_copy_to.py ~/Nextcloud/Music/* ~/Music/")
        sys.exit(1)

    source_dirs = sys.argv[1:-1]
    target_dir = Path(sys.argv[-1]).expanduser().resolve()
    total_files = 0

    print(f"Target directory: {target_dir}\n")
    for source in source_dirs:
        print(f"➤ Processing {source}")
        total_files += process_source(source, target_dir)
        print("\n" + "="*50 + "\n")

    print(f"Finished processing {len(source_dirs)} sources")
    print(f"Total files processed: {total_files}")

if __name__ == "__main__":
    main()
