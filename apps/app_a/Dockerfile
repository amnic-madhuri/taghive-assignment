FROM python:3.10-slim as build
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
build-essential gcc zlib1g

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

FROM python:3.10-slim
RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

USER 999

WORKDIR /usr/app/venv
COPY --chown=python:python --from=build /usr/app/venv /usr/app/venv
COPY --chown=python:python . .
EXPOSE 5000
ENV PATH="/usr/app/venv/bin:$PATH"
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:application" ]