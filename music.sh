#!/bin/bash

# Set your output folder
OUTPUT_DIR="$HOME/YouTubeDownloads"

# Create the output folder if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop until user cancels or submits an empty link
while true; do
    LINK=$(zenity --entry \
        --title="YouTube Playlist Downloader" \
        --text="Enter YouTube playlist link (or leave empty to quit):")

    # Exit if cancelled or blank
    if [[ -z "$LINK" ]]; then
        zenity --info --text="Download session ended."
        break
    fi

    # Confirm download
    zenity --question --text="Download this playlist?\n$LINK"
    if [[ $? -eq 0 ]]; then
        zenity --info --text="Starting download..."

        yt-dlp \
            "$LINK" \
            -x --audio-format mp3 \
            --embed-metadata --add-metadata --embed-thumbnail \
            --download-archive "$OUTPUT_DIR/downloaded.txt" \
            -o "$OUTPUT_DIR/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" \
            2>&1 | zenity --progress --pulsate --auto-close --title="Downloading..."

        zenity --info --text="Finished downloading."
    fi
done
