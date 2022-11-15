FROM python:3.8

ADD hello_world_s3.py .

RUN pip3 install boto3

CMD ["python3","./hello_world_s3.py"]