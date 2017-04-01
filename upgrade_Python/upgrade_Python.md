## Upgrade Python to 3.xx on Linux Server

### Ubuntu 12.04 Server  
  1. Download lastest version from [python.org](https://www.python.org/download)
  2. prepare installation enviroment:
```
apt-get install gcc openssl zlib make checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```
  3. unarchive the package, enter into the installation directory
  4. modify file: "Modules/Setup.dist"  
    uncommon below lines:
```
SSL=/usr/lib/ssl  
_ssl _ssl.c  
-DUSE_SSL -I$(SSL)/include -I$(SSL)  /include/openssl  
-L$(SSL)/lib -lssl -lcrypto
```
  5. configure
  
  > _#这里一定要注意，解压完之后要设置enable-shared参数， 在wsgi.py 在web server中python 才能在apache或者Nginx运行_  
  > 123
```
./configure --enable-shared
``` 
  6. install
```
make #check if there are any warnings or errors  
checkinstall
```
