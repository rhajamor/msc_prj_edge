import paho.mqtt.client as mqtt

import logging
import time

# logging.basicConfig(filename="edge_node0.log", format='%(asctime)s %(message)s', filemode='w')
# logger =logging.getLogger()
# logger.setLevel(logging.DEBUG)

def client_side_execution(client, userdata, message):
    #logger.info("Received message: " + str(message.payload.decode("utf-8")))
    print("Received message: " + str(message.payload.decode("utf-8")))
    #decode de l'objet JSON
    #Maj de l'object JSON avec les données méteo
    
    #rentrauinement du model AI
    #envoie du signal au gestionnaire 
    #envoie de la réponse au Device

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("EdgeNode_1")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = client_side_execution
time.sleep(30)
client.loop_stop()

#while true 
   # if (message == true && Topic =="TEMPERATURE" )
    # client.on_message()