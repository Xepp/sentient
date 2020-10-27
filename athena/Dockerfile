FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y gcc

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --quiet --no-cache-dir -r requirements.txt
EXPOSE 5001

CMD [ "python", "main.py" ]
