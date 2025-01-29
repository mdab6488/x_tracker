#!/bin/sh
# Generate SSL and DH parameters if missing
if [ ! -f "/etc/nginx/ssl/fullchain.pem" ]; then
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/privkey.pem \
    -out /etc/nginx/ssl/fullchain.pem \
    -subj "/CN=localhost"
fi

if [ ! -f "/etc/nginx/ssl/dhparam.pem" ]; then
  openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048
fi

exec "$@"