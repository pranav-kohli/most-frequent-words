FROM python:3.8.4-slim-buster

RUN apt-get update && apt-get clean

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY ./ .


#RUN apt-get install gcc -y
RUN pip3 install -r requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
RUN mkdir -p /uploads

ENV PYTHONPATH="$PYTHONPATH:/"


EXPOSE 5000
CMD python app/app.py
