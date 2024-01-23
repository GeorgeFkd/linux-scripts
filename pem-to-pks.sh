# enter and verify password
openssl pkcs12 -export -in localhost+2.pem -inkey localhost+2-key.pem -out keystore.p12
#to check whether it worked or not
keytool -list -v -keystore keystore.p12 -storetype pkcs12
