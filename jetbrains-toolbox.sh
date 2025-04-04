#!/bin/bash
#OPENSUSE ONLY
# inspired by https://dev.to/janetmutua/installing-jetbrains-toolbox-on-ubuntu-527f
VERSION=2.5.2.35332
echo "Downloading version $VERSION of jetbrains toolbox"
wget -c https://download.jetbrains.com/toolbox/jetbrains-toolbox-$VERSION.tar.gz
sudo tar -xzf jetbrains-toolbox-$VERSION.tar.gz -C /opt
echo "Downloading additional library libgthread-2_0-0"
sudo zypper install libgthread-2_0-0

echo "run /opt/jetbrains-toolbox-$VERSION/jetbrains-toolbox to run the app"

