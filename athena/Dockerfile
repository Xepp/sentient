FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y gcc g++

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
