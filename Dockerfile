FROM python:3.5

ADD . /nc99.co
WORKDIR /nc99.co
RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /nc99.co/nc99
CMD ["gunicorn", "--bind=0.0.0.0", "nc99.wsgi"]
