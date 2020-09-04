import paho.mqtt.client as mqtt
import logging

from listen_house_config import config

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

MQTT_BROKER = config["mqtt_broker"]
MQTT_TOPIC = config["mqtt_topic"]
MQTT_PORT = config["mqtt_port"]

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print('Connected.')
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    m = msg.payload.decode('utf-8')
    print(msg.topic + " | " + m)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_forever()
