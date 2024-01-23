#!/bin/bash

# Path to the renewed certificate
CERT_PATH="/etc/letsencrypt/live/yourdomain.com/fullchain.pem"
KEY_PATH="/etc/letsencrypt/live/yourdomain.com/privkey.pem"
PKCS12_PATH="/path/to/keystore.p12" # Update this to your keystore path

# Convert the renewed certificate to PKCS12 format
sudo openssl pkcs12 -export -in $CERT_PATH -inkey $KEY_PATH -out $PKCS12_PATH -name springboot -CAfile chain.pem -caname root -password pass:your-keystore-password

# Restart Spring Boot Application
# This command depends on how you run your Spring Boot app. 
# For example, if you're using a systemd service:
sudo systemctl restart your-spring-boot-app.service
chmod +x renew-certificate.sh

nano /etc/letsencrypt/renewal/yourdomain.com.conf
post_hook = /path/to/renew-certificate.sh
# for testing purposes
sudo certbot renew --dry-run
