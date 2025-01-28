#!/bin/sh
# Generate SSL if missing
if [ ! -f "/etc/nginx/ssl/fullchain.pem" ]; then
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/privkey.pem \
    -out /etc/nginx/ssl/fullchain.pem \
    -subj "/CN=localhost"
fi

exec "$@"