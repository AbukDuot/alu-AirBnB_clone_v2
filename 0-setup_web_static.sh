#!/usr/bin/env bash
# web static development
ssh -i /root/.ssh/id_rsa ubuntu@107.20.20.164 <<EOF
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Hello, this is a test HTML file." | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '44i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
EOF
