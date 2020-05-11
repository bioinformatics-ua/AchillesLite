FROM python:3.7

RUN pip install SQLAlchemy==1.3.16

RUN alias ll="ls -l"

WORKDIR /AchillesLite

CMD tail -f >> /dev/null