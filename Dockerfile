FROM python:3

RUN pip install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 install flask
RUN pip3 install requests

EXPOSE 5001

ENTRYPOINT ["python3"]

CMD ["res.py"]

