## Homework 3 - Internet of Things 101
## Goal: Capture faces in a video stream coming from the edge in real time, transmit them to the cloud in real time, and save these faces in the cloud for long term storage.

### Procedures on NVIDIA Jetson TX2:
1. Build docker image for face detection
```
sudo docker build -t face_detector -f Dockerfile.detector .
```
2. Build docker image for message forwarding
```
sudo docker build -t forwarder -f Dockerfile.forwarder .
```
3. Create network bridge
```
sudo docker network create --driver bridge hw03
```
4. Create an alpine linux based mosquitto container as the local broker
```
docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh
# inside the container, install and run mosquitt
apk update && apk add mosquitto
/usr/sbin/mosquitto
```
5. Creat a container for face detection
```
sudo docker run --name face_detector --network hw03 --device=/dev/video1:/dev/video1 -ti face_detector /bin/bash
# inside the container, run program to detect faces from the web cam.
python3 face_detection.py
```
6. Creat a container for message forwarding
```
sudo docker run --name forwarder --network hw03 -ti forwarder sh
# inside the container, run program to forward message from the local broker to the cloud broker
python3 forwarder.py
```
### Procedures on IBM Cloud VSI:
1.  Create network bridge
```
sudo docker network create --driver bridge hw03
```
2. Create docker image for saving face images
```
sudo docker build -t cloud_saver -f Dockerfile.cloud_saver .
```
3. Create an alpine linux based mosquitto container as the cloud broker
```docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh
# inside the container, install and run mosquitt
apk update && apk add mosquitto
/usr/sbin/mosquitto
```

