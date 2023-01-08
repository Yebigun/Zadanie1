FROM python:3

WORKDIR '/app'

COPY main.py main.py

CMD [ "python3", "./main.py"]