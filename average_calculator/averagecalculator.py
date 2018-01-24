import paho.mqtt.client as mqttClient
import time
import config
import requests


#define array for storing numbers in last 5 second
arr =[]

def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("Connected to broker")

        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:

        print("Connection failed")


def on_message(client, userdata, message):
    arr.append(int(message.payload))




mqtt_client = mqttClient.Client()  # create new instance
mqtt_client.on_connect = on_connect  # attach function to callback for connec
mqtt_client.on_message = on_message  # attach function to callback for receiving message

#Connect and subscribe to queue
mqtt_client.connect(config.MQTT_HOST, config.MQTT_PORT)  # connect to broker
mqtt_client.loop_start()  # start the loop
mqtt_client.subscribe(config.MQTT_TOPIC)

#start time
start = time.time()
try:
    while True:
        if len(arr)>0  and time.time() -start > 5:
            #if 5 seconds is expired
            #Calculate average of last five secons
            average = sum(arr) /len(arr)

            #send average to API
            r = requests.post('http://0.0.0.0:8000/api/values/', json={"value": average})
            #Reset array
            arr = []
            #Start timer again
            start = time.time()
except Exception as e:
    print (str(e))
    mqtt_client.disconnect()
    mqtt_client.loop_stop()

