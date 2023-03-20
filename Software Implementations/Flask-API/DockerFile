FROM python:3.11

RUN apt-get update

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
