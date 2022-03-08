FROM public.ecr.aws/lambda/python:3.8

COPY ./config/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./config/prod/requirements_prod.txt ./requirements_prod.txt
RUN pip install -r requirements_prod.txt

ADD MyApp ${LAMBDA_TASK_ROOT}/MyApp
COPY aws_handler.py ./MyApp/aws_handler.py

CMD ["MyApp.main.handler"]