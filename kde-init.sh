mkdir -p ~/.local/share
git clone https://invent.kde.org/sdk/kdesrc-build.git ~/.local/share/kdesrc-build
mkdir -p ~/.local/bin
ln -sf ~/.local/share/kdesrc-build/kdesrc-build ~/.local/bin
export PATH=$PATH:~/.local/bin
# this is to check that it has been installed properly
# if you havent ran kdesrc-build --initial-setup it will have some errors
# kdesrc-build to check if it is ok 
kdesrc-build --initial-setup
