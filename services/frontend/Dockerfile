FROM node:18-alpine

RUN apk update && apk add --no-cache make git

WORKDIR /frontend

RUN npm i npm@latest -g && \
	npm install -g @angular/cli@latest

COPY . /frontend

RUN npm install

CMD ["ng", "serve", "--host", "0.0.0.0"]