FROM alpine:3.7 AS buildbot-build

RUN \
    apk add --no-cache \
        python3
COPY . /

CMD ["sh","-c","python3 /tinysrv2.py"]