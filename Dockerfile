FROM debian:sid

RUN apt-get -y update; \
    apt-get install -y python-requests python-anyjson python-simplejson

ADD ./registry_cleanup.py /bin/cleanup

ENTRYPOINT ["/bin/cleanup"]
