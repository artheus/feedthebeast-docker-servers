FROM ftbbase

ARG DOWNLOAD_URL=https://addons-origin.cursecdn.com/files/2482/845/FTBBeyondServer_1.11.0.zip
ARG ZIP_NAME=ftbbeyond-server.zip

WORKDIR /home/minecraft/mcmyadmin/Minecraft
COPY gen_server_properties.sh ./

RUN	wget -O $ZIP_NAME $DOWNLOAD_URL && \
	unzip $ZIP_NAME && \
	rm $ZIP_NAME

RUN . ./settings.sh && \
	mv $FORGEJAR ftbserver.jar && \
	/bin/sh ./FTBInstall.sh && \
	echo "eula=true" > eula.txt

RUN /bin/sh ./gen_server_properties.sh && \
	rm gen_server_properties.sh

WORKDIR /home/minecraft/mcmyadmin