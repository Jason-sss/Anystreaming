## Install Tomcat and Java in Linux Server
### Install versions: 
> java: 1.7.0_80  
> Tomcat: 7.0
### packges
> jdk-7u80-linux-x64.tar.gz  
> apache-tomcat-7.0.69.tar.gz
### Installation
####  Java:
```sh
tar -zxvf jdk-7u80-linux-x64.tar.gz
mv jdk1.7.0_80 /usr/java1.7
vi /etc/profile # add below to the end
	export JAVA_HOME=/usr/java1.7
	export JAVA_BIN=$JAVA_HOME/bin
	export PATH=$PATH:$JAVA_HOME/bin
	export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
source /etc/profile
```

#### Tomcat:
```sh
tar -zxvf apache-tomcat-7.0.69.tar.gz
mv apache-tomcat-7.0.69 /usr/local/tomcat7
```

#### NOTE:
>check JAVA version: 
```sh
java -version
```

>start/stop tomcat: 
```sh
/usr/local/tomcat7/bin/startup.sh  
/usr/local/tomcat7/bin/shutdown.sh
```
