FROM openjdk:8-jre

COPY sf3-1.10.2-3.0.6.zip /srv/server.zip
COPY entry.sh /srv/entry.sh

WORKDIR /srv

RUN unzip server.zip && \
    rm server.zip && \
    echo "eula=TRUE" > eula.txt && \
    /bin/bash FTBInstall.sh && \
    chmod +x ServerStart.sh

EXPOSE 25565

CMD ["/bin/bash","entry.sh"]