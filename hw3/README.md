## Homework 3 - Internet of Things 101
## Goal: Capture faces in a video stream coming from the edge in real time, transmit them to the cloud in real time, and save these faces in the cloud for long term storage.

### Procedures on NVIDIA Jetson TX2:
#### 1. Build docker image for face detection
```sudo docker build -t face_detector -f Dockerfile.detector .```
#### 2. Build docker image for message forwarding
```sudo docker build -t forwarder -f Dockerfile.forwarder .```
#### 3. Create network bridge
```sudo docker network create --driver bridge hw03```
#### 4. Create an alpine linux based mosquitto container as the local broker
```docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh```
  Once inside the container, install and run mosquitto
  ```
  apk update && apk add mosquitto
  /usr/sbin/mosquitto
  ```
