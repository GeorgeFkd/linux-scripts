sudo apt install libnss3-tools
curl -s https://api.github.com/repos/FiloSottile/mkcert/releases/latest | grep browser_download_url | grep '\linux-amd64' | cut -d '"' -f 4 | wget -i -
sudo mv mkcert-v*-linux-amd64 /usr/bin/mkcert
sudo chmod +x /usr/bin/mkcert
mkcert --version
