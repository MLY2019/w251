import paho.mqtt.client as mqtt 


def on_message(client, userdata, msg):
    print("message received!")
    msg = msg.payload
    cloud_client.publish("faces_forwarded", payload = msg, qos = 0, retain = False)
    print("message published to cloud broker!")

#Create a new instance of client and connect to the remote broker.
cloud_client=mqtt.Client()
cloud_client.connect("169.45.122.103", 1883, 60)

#Create a new instance of client on jetson and connect to the local broker.
client = mqtt.Client()
client.connect("172.18.0.2", 1883, 60)

client.on_message=on_message

#subscribe to the jetson topic.
client.subscribe("faces_detected")

client.loop_forever() 




   




