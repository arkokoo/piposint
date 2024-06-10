FROM node:21-alpine

RUN npm install -g http-server

WORKDIR /app

COPY ./app .

RUN npm install

RUN npm run build

EXPOSE 8080

CMD [ "http-server", "dist" ]