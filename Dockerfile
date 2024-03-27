FROM python:alpine

ADD app.py requirements.txt code/
ADD templates code/templates
ADD static code/static
WORKDIR /code
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]