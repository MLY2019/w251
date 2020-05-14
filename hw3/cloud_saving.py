import numpy as np
import cv2 
import paho.mqtt.client as mqtt

index = 0
path = '/data/'

def on_message(client, userdata, msg):
    print('message received on cloud!')
    global index
    global path
    f = np.frombuffer(msg.payload, dtype='uint8')
    jpg = cv2.imdecode(f, flags=1)
    name = 'face_%s.png'%str(index)
    cv2.imwrite(path+name, jpg)
    print('message saved to cloud object storage!')
    index += 1

# Create a new instance of client on cloud and connect to the cloud broker
client = mqtt.Client()
client.connect('172.18.0.2',1883,60)

client.on_message=on_message

# Subscribe to the cloud topic.
client.subscribe('faces_forwarded')

client.loop_forever()






   




