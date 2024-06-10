FROM nginx:alpine

ADD settings/default.conf /etc/nginx/conf.d/default.conf

# ADD 404.html /var/www/html/404.html

RUN apk update && apk upgrade && apk add --no-cache openssl

RUN sed -i \
    -e 's#access_log /var/log/nginx/access\.log#access_log /dev/stdout/#' \
    -e 's#error_log /var/log/nginx/error\.log#error_log /dev/stderr/#' \
    /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/ssl

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt -subj "/C=FR/ST=Paris/L=Paris/O=42/OU=42/CN=localhost"

EXPOSE 443