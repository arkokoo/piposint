FROM node:21-alpine

RUN apk add --no-cache git

WORKDIR /app

RUN git clone https://github.com/tyrasd/overpass-turbo.git .

COPY ./app .

RUN yarn install
RUN yarn build

# Lancer l'application
CMD [ "yarn", "run", "start", "--host" ]