#!/usr/bin/env bash

# Update package repository and install nginx
apt update -y
apt install nginx -y

ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a \
        location /hbnb_static/ { \
            alias /data/web_static/current/; \
        }' /etc/nginx/sites-available/default
service nginx restart
