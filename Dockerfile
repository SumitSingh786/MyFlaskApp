FROM python:3.8-slim-bullseye
WORKDIR /usr/src/FlaskApp
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT FLASK_APP=/usr/src/FlaskApp/app.py flask run --host=0.0.0.0