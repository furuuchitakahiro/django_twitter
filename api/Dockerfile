FROM python:3.7.2
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
ENV HOME=/usr/src/app
WORKDIR $HOME

ADD mytwitter $HOME
ADD requirements.txt $HOME
RUN pip install -r requirements.txt
