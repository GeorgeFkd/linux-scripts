nohup mvn spring-boot:run > output-2.log 2>&1 &
tail -f output-2.log | less
