FROM alpine:latest

# Install dependencies
RUN apk update \
    && apk add --no-cache wget unzip openjdk8-jre bash \
    && mkdir -p /opt/minecraft

WORKDIR /opt/minecraft

EXPOSE 25565
