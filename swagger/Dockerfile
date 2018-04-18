FROM python:3-onbuild

MAINTAINER Naveen Kaul <nkaul@iu.edu>

#ENV HOME  /
#ENV PYENV_ROOT /.pyenv
#ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN make dirs

RUN make swagger

# Get updates 
RUN apt-get update	

# install java
RUN apt-get install -q -y default-jre

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64 #This can vary
ENV PATH $PATH:$JAVA_HOME/bin
# install net tools
RUN apt-get install -q -y net-tools
  
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

RUN make train

# Install the flask service using make commands
RUN make service

# start the service
CMD ["make", "start"]