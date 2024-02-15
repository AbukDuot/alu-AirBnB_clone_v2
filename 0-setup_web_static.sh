#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install nginx
sudo service start nginx

mkdir -p /data/web_static/releases/test/
sudo cat > /data/web_static/releases/test/index.html <<<"<html>
  <head>
  </head>
  <body>
<!--this code wont work without my name-->
    Humphrey Nyahoja
  </body>
</html>"

