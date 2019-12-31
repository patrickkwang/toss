FROM python:3.8.1-buster

# install basic tools
RUN apt-get update
RUN apt-get install -yq \
    vim

# set up murphy
RUN mkdir /home/murphy
ENV HOME=/home/murphy
ENV USER=murphy
WORKDIR /home/murphy

# install requirements
ADD ./requirements.txt /home/murphy/requirements.txt
RUN pip install -r /home/murphy/requirements.txt --src /usr/local/src

# install library
ADD ./toss /home/murphy/toss
ADD ./main.py /home/murphy/main.py
ADD ./setup.py /home/murphy/setup.py
RUN pip install -e .

# setup entrypoint
ENTRYPOINT ["/home/murphy/main.py"]