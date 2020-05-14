import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
from time import sleep

sensor = Adafruit_DHT.DHT22
serverIP = sys.argv[1]

print("Sending signals to " + serverIP)

# Connect to broker
mqttClient = mqtt.Client("djad_mqtt")
mqttClient.connect(serverIP, 1883)
mqttClient.loop_start()

pin = 4
print("[press ctrl+c to end the script]")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        sleep(2.5)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
            mqttClient.publish("cabin/temp", temperature)
            mqttClient.publish("cabin/humidity", humidity)
        else:
            print("Failed to get reading.")

except KeyboardInterrupt:
    print("End")
    
