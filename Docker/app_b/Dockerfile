FROM python:3

WORKDIR /app

RUN apt-get update && \
        apt-get install -y sqlite3

COPY files/schema.sql .
RUN sqlite3 database.db < schema.sql

COPY files/app_b.py .
COPY files/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD [ "python", "./app_b.py" ]
