import paho.mqtt.client as mqtt
import logging

from listen_house_config import config

MQTT_BROKER = config["mqtt_broker"]
MQTT_TOPIC = config["mqtt_topic"]
MQTT_PORT = config["mqtt_port"]
MQTT_LOG = config["mqtt_log"]

logging.basicConfig(filename=MQTT_LOG, level=logging.DEBUG)

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print('Connected.')
    logging.debug(logging.DEBUG)
    logging.debug(userdata)
    logging.debug(flags)
    logging.debug(rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    m = msg.payload.decode('utf-8')
    print(msg.topic + " | " + m)

client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_forever()
