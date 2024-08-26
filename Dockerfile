FROM python:3.10.12
WORKDIR /app

COPY ./src/app /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 8010

CMD ["flask", "run", "--host=0.0.0.0", "--port=8010"]