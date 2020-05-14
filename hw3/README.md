## Homework 3 - Internet of Things 101
### Goal: Capture faces in a video stream coming from the edge in real time, transmit them to the cloud in real time, and save these faces in the cloud for long term storage.

### Procedures on NVIDIA Jetson TX2:
#### 1. Build docker image for face detection
```sudo docker build -t face_detector -f Dockerfile.face_detector .```
#### 2. Build docker image for message forwarding
```sudo docker build -t forwarder -f Dockerfile.forwarder .```
#### 1. Create network bridge
```sudo docker network create --driver bridge hw03```
