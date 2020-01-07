var express = require('express');
var app = express();
var cors = require('cors');
var mqtt = require('mqtt');

// Create the web app
var app = express();
app.use(cors());

// Create the MQTT client
var mqttclient = mqtt.connect('mqtt://localhost');

// Local value of temperature
var tempValue = 0;

// Start server
var server = app.listen(9080, function () {
   var host = server.address().address;
   var port = server.address().port;
   console.log("App listening at http://%s:%s", host, port);
})

// On connect to MQTT broker
mqttclient.on('connect', function() {
    console.log('Connected to MQTT Broker');
    mqttclient.subscribe('djad.temp', function(err) {
    });
});

mqttclient.on('message', function(topic, message) {
    tempValue = message;
});

app.get('/temp', function(req, res) {
    res.json("{temp:" + tempValue + "}");
});

