import paho.mqtt.client as mqtt
from random import randrange, uniform
import logging
import time

# logging.basicConfig(filename="rasperry_dev0.log", format='%(asctime)s %(message)s', filemode='w')
# logger =logging.getLogger()
# logger.setLevel(logging.DEBUG)



mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

# encodage en JSON du  modele de données 

while True:
    #JSON to string
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    # logger.debug("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
