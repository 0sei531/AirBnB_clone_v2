#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

set -e  # Exit script immediately if any command exits with a non-zero status
exec 2>> /var/log/web_server_setup.log  # Redirect stderr to a log file for detailed logging

echo "Updating package lists..."
apt-get update

echo "Installing Nginx..."
apt-get install -y nginx

echo "Creating directories..."
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Creating index.html file..."
echo "Holberton School" > /data/web_static/releases/test/index.html

echo "Creating symbolic link..."
ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "Setting ownership and permissions..."
chown -R ubuntu /data/
chgrp -R ubuntu /data/

echo "Configuring Nginx..."
cat > /etc/nginx/sites-available/default <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
EOF

echo "Restarting Nginx..."
service nginx restart

echo "Web server setup completed successfully."

