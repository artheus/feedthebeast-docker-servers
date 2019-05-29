FROM feedthebeast/ftbbase

ARG DOWNLOAD_URL
ARG DYNMAP_URL

COPY setup.sh ./
RUN /bin/bash -ex setup.sh && \
    rm setup.sh

ENTRYPOINT ["/bin/sh", "ServerStart.sh"]
