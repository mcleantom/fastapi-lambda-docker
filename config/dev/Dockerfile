FROM python:3.8

WORKDIR /usr/src/fastapi-lambda-docker

COPY ./config/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./config/dev/requirements_dev.txt ./requirements_dev.txt
RUN pip install -r requirements_dev.txt

COPY ./MyApp ./MyApp

CMD ["uvicorn", "MyApp.main:api", "--host", "0.0.0.0", "--port", "8000", "--reload"]