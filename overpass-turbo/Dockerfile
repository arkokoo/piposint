FROM node:21-alpine

RUN apk add --no-cache git

RUN npm install -g http-server

WORKDIR /app

RUN git clone https://github.com/tyrasd/overpass-turbo.git .

COPY ./app .

RUN npm install
RUN npm run build

# Lancer l'application
CMD [ "http-server", "dist" ]
