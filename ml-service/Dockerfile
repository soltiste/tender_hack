FROM python:3.10.5

WORKDIR /ml-service

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY startup.sh ./startup.sh
RUN chmod 777 ./startup.sh && \
    sed -i 's/\r//' ./startup.sh

COPY main.py .
COPY api api

ENTRYPOINT ["./startup.sh"]
