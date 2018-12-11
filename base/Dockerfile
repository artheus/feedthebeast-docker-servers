FROM alpine:latest

ARG MCMA_ETC_URL=http://mcmyadmin.com/Downloads/etc.zip
ARG MCMA_DOWNLOAD_URL=http://mcmyadmin.com/Downloads/MCMA2_glibc26_2.zip

ENV MCMA_PASSWORD=${MCMA_PASSWORD:-pass123}

# Install dependencies
RUN apk update \
    && apk add --no-cache wget unzip openjdk8-jre bash

# Configure
RUN wget -nv $MCMA_ETC_URL -O /usr/local/etc.zip \
	  && unzip /usr/local/etc.zip -d /usr/local \
	  && rm /usr/local/etc.zip \
    && mkdir -p /opt/minecraft

WORKDIR /opt/minecraft

EXPOSE 25565
