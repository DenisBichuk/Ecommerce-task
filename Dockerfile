FROM python:3.12-slim

WORKDIR /app

RUN apt update; apt install -y netcat-openbsd

COPY . .

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
