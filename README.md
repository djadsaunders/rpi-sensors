# RPI Sensors

A Raspberry Pi can easily be turned into an IOT device to collect readings from the environment.

This project collects temperature and humidity values from a sensor attached to a Raspberry Pi and sends to an MQTT broker where a Node.JS app is listening and exposing sensor values over HTTP as JSON objects.

Once those values are available, they can consumed in a variety of ways, for instance via a web UI or a Node Red workflow or dashboard.

**Technologies used**

* Python
* Mosquitto
* Node.JS

See the Wiki for more details..
