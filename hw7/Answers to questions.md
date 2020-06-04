#### Describe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve?
I loaded a pre-trained SSD model to capture faces from the web cam on Jetson. I cropped the original image to contain only the face. Then the face was sent to the local borker for publishing.
The SSD model I used is based on mobilenet and it was tained on WIDERFACE dataset. It achieves an accuracy of above 0.9 on the sample image. 

#### Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?
It achieved reasonable accuracy in my expirial tests although when the object is moving the accuracy drops significantly. I probably will not use this solution to develop a robust, production-grade system.

#### What framerate does this method achieve on the Jetson? Where is the bottleneck?

#### Which is a better quality detector: the OpenCV or yours?
Mine is better.
