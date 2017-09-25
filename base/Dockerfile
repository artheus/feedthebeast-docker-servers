FROM ubuntu:16.04

RUN apt-get update && \
	apt-get install -y wget unzip openjdk-8-jre

RUN useradd minecraft -m -s /bin/bash

WORKDIR /usr/local
RUN wget http://mcmyadmin.com/Downloads/etc.zip && \
	unzip etc.zip && \
	rm etc.zip

COPY McMyAdmin.conf /home/minecraft/mcmyadmin/
WORKDIR /home/minecraft/mcmyadmin
RUN wget http://mcmyadmin.com/Downloads/MCMA2_glibc26_2.zip && \
	unzip MCMA2_glibc26_2.zip && \
	rm MCMA2_glibc26_2.zip && \
	mkdir Minecraft && \
	./MCMA2_Linux_x86_64 -nonotice -updateonly


RUN chown -R minecraft:minecraft /home/minecraft

EXPOSE 8080
EXPOSE 25565

USER minecraft

ENTRYPOINT ["/home/minecraft/mcmyadmin/MCMA2_Linux_x86_64"]
CMD ["-setpass", "pass123"]