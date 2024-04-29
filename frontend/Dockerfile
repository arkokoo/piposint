FROM node:21-alpine

WORKDIR /app

COPY ./app .

RUN npm install
RUN npm run build

#EXPOSE 4173

# Lancer l'application
CMD [ "npm", "run", "preview" ]