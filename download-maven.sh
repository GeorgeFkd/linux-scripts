curl -O https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz
tar -xvzf apache-maven-3.9.6-bin.tar.gz
sudo mv apache-maven-3.9.6 /opt/
nano ~/.bashrc
export M2_HOME=/opt/apache-maven-3.9.6
export PATH=$M2_HOME/bin:$PATH
source ~/.bashrc
mvn -version
