FROM node:alpine

WORKDIR /app
EXPOSE 3000

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install -g react-scripts
RUN npm install react-router-dom
RUN npm install sass

COPY . ./

CMD ["npm", "start"]
