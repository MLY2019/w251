## Homework 3 - Internet of Things 101

### Goal: 
Capture faces in a video stream coming from the edge in real time, transmit them to the cloud in real time, and save these faces in the cloud for long term storage.

### Architecture and flow: 
In this IoT architecture, we have two mosquitto broker containers, one on Jetson TX2 and one on cloud VSI, for message receiving and publishing. On TX2, we have a container that connects to the web cam, detects faces and sends face images to the TX2 mosquitto broker and another container that forwards face images to the cloud mosquitto broker. On cloud VSI, we have a container that receives face images from the cloud moquitto broker and saves them to the cloud object storage bucket. 

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
1. Create docker image for saving face images
```
docker build -t cloud_saver -f Dockerfile.cloud_saver .
```
2.  Create network bridge
```
docker network create --driver bridge hw03
```

3. Create an alpine linux based mosquitto container as the cloud broker
```
docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh
# inside the container, install and run mosquitt
apk update && apk add mosquitto
/usr/sbin/mosquitto
```
4. Mount the cloud object storage bucket to the VSI

  	4.1 Install s3fs on VSI
    ```
    apt-get update
    apt-get install automake autotools-dev g++ git libcurl4-openssl-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
    git clone https://github.com/s3fs-fuse/s3fs-fuse.git
    cd s3fs-fuse
    ./autogen.sh
    ./configure
    make
    ```
    4.2 Enter ```<service instance id>:<api key>``` as credentials and set owner-only permissions
    ```
    nano /$HOME/.cos_creds
    chmod 600 $HOME/.cos_creds
    ```
    4.3 Create a directory on VSI as the mounting point
    ```
    mkdir /mnt/hw3_bucket
    ```
    4.4 Mount the existing bucket "face-images" to the mounting point
    ```
    s3fs face-images /mnt/hw3_bucket -o nonempty -o passwd_file=$HOME/.cos_creds -o ibm_iam_auth -o url=https://s3.us.cloud-object-storage.appdomain.cloud -o use_path_request_style
    ```
5. Creat a container for message saving
```
docker run --name cloud_saver -v /mnt/hw3_bucket:/data --network hw03 -ti cloud_saver sh
# inside the container, run the message saving program
python3 cloud_saving.py
```



