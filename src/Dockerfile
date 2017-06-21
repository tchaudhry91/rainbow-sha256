FROM python:3-alpine

RUN mkdir -p /rainbow-hasher-sha256

ADD . /rainbow-hasher-sha256

RUN pip install -r rainbow-hasher-sha256/requirements.txt

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

EXPOSE 9999

WORKDIR /rainbow-hasher-sha256

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:9999", "--workers", "4", "main:app"]

HEALTHCHECK --interval=3s --timeout=3s \
  CMD curl http://localhost:9999/reverse_hash?str="test" || exit 1
