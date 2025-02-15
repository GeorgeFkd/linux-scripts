#!/bin/bash

data=$(flatpak list --app)

echo "$data" | awk '{for (i=1; i<=NF; i++) if ($i ~ /^org\./) print $i}' > flatpak-apps.txt
