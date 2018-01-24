# Import package
import paho.mqtt.client as mqtt
from random import randint
import time
import config



# Define on_publish event function
def on_publish(client, data, mid):
    print ("Sent")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed")


def main():
    # Initiate MQTT Client
    mqtt_client = mqtt.Client()

    # Register publish callback function
    mqtt_client.on_publish = on_publish

    # Connect with MQTT Broker
    mqtt_client.connect(config.MQTT_HOST, config.MQTT_PORT, keepalive=1)

    while True:
        mqtt_client.loop_start()  # start the loop
        #Generate random number
        number = randint(0, 10000)

        print("Sending :  " +str(number))
        #Publis number to mqtt
        mqtt_client.publish(config.MQTT_TOPIC, number)

        #wait for 100 ms
        time.sleep(0.1)


if __name__ == "__main__":
	main()

