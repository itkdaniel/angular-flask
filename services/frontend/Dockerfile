FROM node:18-alpine as builder

RUN apk update && apk add --no-cache make git

# install app dependencies
# set working directory
WORKDIR /frontend
#WORKDIR /usr/src/app

ENV PATH /frontend/node_modules/.bin:$PATH
COPY package.json /frontend/package.json

RUN npm i npm@latest -g && \
	npm install -g @angular/cli@latest

# set environment variables
ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

COPY . /frontend
# COPY . /usr/src/app

RUN npm install
RUN ng build

CMD ["ng", "serve", "--host", "0.0.0.0"]


#########
# FINAL #
#########

# base image
FROM nginx:1.25.1-alpine

# update nginx conf
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

# copy static files
COPY --from=builder /frontend/dist/ /usr/share/nginx/html

# expose port
EXPOSE 80

# run nginx
#CMD ["nginx"]
CMD ["nginx", "-g", "daemon off;"]