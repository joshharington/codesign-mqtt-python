import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(rc)   
    if rc==0:
        print("connected ok")
        data = {
                "message": "I connected!"
        }
        mqtt.publish("device/connected", data)

def on_message(client, userdata, message):
    print("Message Received")
    print(message)

    if message.retain!=1:
        print("This is a new message")
                                
    if message.retain==1:
        print("This is a retained message")

def process():
        mqtt.Client.connected_flag=False
        client = mqtt.Client("asdqweasd", True, None, mqtt.MQTTv31)
        client.on_connect= on_connect
        client.on_message= on_message
        client.connect("broker.hivemq.com", port=1883, keepalive=60, bind_address="")
        client.loop_start()
        client.subscribe("test-command")

        while True:
                time.sleep(1) # wait


process()