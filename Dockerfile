FROM python:3.11.3-alpine

LABEL Name=fritz_datacollector
EXPOSE 8000
ENV PIP_NO_CACHE_DIR="true"

WORKDIR /app

RUN mkdir -p /donations
COPY requirements.txt /app/
RUN pip install -r requirements.txt && \
    mkdir /etc/fritz

COPY fritz_datacollector/ /app/fritz_datacollector

ENTRYPOINT ["python", "-m", "fritz_datacollector"]
