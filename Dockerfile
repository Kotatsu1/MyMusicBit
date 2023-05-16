FROM python:3.10.11-slim-buster

COPY . .
RUN sudo apt install ffmpeg -y
RUN pip install -r requirements.txt

CMD 'python' 'main.py'