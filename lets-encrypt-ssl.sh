sudo apt install certbot
sudo certbot certonly --standalone -d yourdomain.com
cd /etc/letsencrypt/live/yourdomain.com/
sudo openssl pkcs12 -export -in fullchain.pem -inkey privkey.pem -out keystore.p12 -name springboot -CAfile chain.pem -caname root

#application.properties
server.ssl.key-store=classpath:keystore.p12
server.ssl.key-store-password=your-keystore-password
server.ssl.key-store-type=PKCS12
server.ssl.key-alias=springboot
