FROM ubuntu

# Install Mosquitto and NodeJS
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-add-repository -y ppa:mosquitto-dev/mosquitto-ppa
RUN apt-get install -y mosquitto mosquitto-clients
RUN apt-get install -y nodejs

# Copy services
RUN mkdir /opt/app
WORKDIR /opt/app
COPY main.js .

# Container starts with running Mosquitto broker
ENTRYPOINT service mosquitto start && bash
