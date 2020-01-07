# RPI Sensors

This project collects data from sensors attached to a Raspberry PI and sends to an MQTT broker where a Node.JS app is listening and exposing sensor values over HTTP.

### On the RaspberryPI

This assumes assumes that there is a PI with sensor(s) attached on the local network.

The file cabin-temp.py is a Python script which runs on the PI and reads 2 values (temperature and humidity) from pin 4 every few seconds. These values are automatically provided by the sensor used in this case.

The script then connects to the MQTT broker on the server and sends the temperature and humidity values to 2 topics.

### On the server

Mosquitto provides the MQTT server in this case and needs to be running on the server.

A Node.JS app attaches as an MQTT client and exposes the URL /temp on port 9080. Hitting this URL will return the temperature value in a JSON object.

### Visualizing

I have used Node Red to show the value returned by the Node.JS app in a dashboard.

### Questions/To Do

* I cannot remember which server components are running on the command line and which run in Docker. There is a Docker file to run MQTT and the Node.JS app but not sure if it was used in the end.
* The Node.JS app only seems to read the temperature but this is odd as the dashboard was definitely showing temperature and humidity. Could be that the app is out of date?

