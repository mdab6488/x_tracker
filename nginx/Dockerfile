FROM nginx:1.23-alpine

# Install tools
RUN apk add --no-cache \
    bash \
    certbot \
    openssl

# Copy custom configurations
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY ssl /etc/nginx/ssl

# Custom entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]