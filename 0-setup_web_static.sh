#!/usr/bin/env bash
#Script to deploy static web pages

#install nginx, check for config
if ! which nginx > /dev/null; then
    apt-get update && apt-get install nginx -y
   fi

#create directories
if [[ ! -e /data/web_static/releases/test]]; then
    mkdir -p /data/web_static/releases/test
fi

if [[ ! -e /data/web_static/shared ]]; then
    mkdir -p /data/web_static/shared
    echo "<html>
      <head>
      </head>
      <body>
        Holberton School
      </body>
    </html>" > /data/web_static/releases/test/index.html
fi

#create symlink, removing if exists
if [[ -e /data/web_static/current ]]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
#add /hbnb_static to default

if ! grep -q "hbnb_static" /etc/nginx/sites-availabel/default; then
  line='\\n\tlocation /hbnb_static {\n\t\t alias /data/web_static/current/;\n\t}'
  sed -i "37i $line" /etc/nginx/sites-available/default
fi

service nginx restart
