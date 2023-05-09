FROM python:3.11.2-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY server/ .

EXPOSE 8080

CMD ["python", "app.py"]