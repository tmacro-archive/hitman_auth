FROM tmacro/python:latest

ENV PORT 80
ENV MODE prod
EXPOSE 80

ADD ./requirements.txt /tmp/
RUN apk_add py3-psycopg2 ca-certificates && \
	update-ca-certificates && \
	apk_add --virtual build gcc python3-dev build-base && \
	pip install -r /tmp/requirements.txt && \
	apk del build

ADD s6 /etc

ADD . /app

ENTRYPOINT ["/init"]

