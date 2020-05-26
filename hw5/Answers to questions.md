#### 1. What is TensorFlow? Which company is the leading contributor to TensorFlow?
TensorFlow is a deep learning framework based on Keras. Google is the leading contributor to TensorFlow.

#### 2. What is TensorRT? How is it different from TensorFlow?
NVIDIA TensorRT is an SDK for high-performance deep learning inference. It includes a deep learning inference optimizer and runtime that delivers low latency and high-throughput for deep learning inference applications. 

While TensorFlow has flexibility running on CPU, GPU or TPU, TensorRT is a GPU only platform but its performance on GPU is superior. 

#### 3. What is ImageNet? How many images does it contain? How many classes?
ImageNet is an image dataset organized according to the WordNet hierarchy. 

ImageNet contains a total of 14,197,122 images in 21841 classes.

#### 4. Please research and explain the differences between MobileNet and GoogleNet (Inception) architectures.
GoogleNet is a 27 layers deep convolutional neural network. Within the 27 layers there is a module called inception which is a combination of a 1×1 Convolutional layer, a 3×3 Convolutional layer and a 5×5 Convolutional layer with their output filter banks concatenated into a single output vector forming the input of the next stage. Besides, there are two major add-ons in the original inception module: (1) a 1×1 Convolutional layer before applying another layer, which is mainly used for dimensionality reduction and (2) a parallel Max Pooling layer, which provides another option to the inception layer.

In the Mobile Net architecutre, only the first layer uses the regular convolution. Instead, the next layers use the depthwise separable convolutions which are the combination of the depthwise and pointwise convolution. The depthwise convolution does the convolution on each channel separately. If the image has three channels, therefore, the output image also has three channels. This depthwise convolution is used to filter the input channels. The next step is the pointwise convolution, which is similar to the regular convolution but with a 1x1 filter. The purpose of pointwise convolution is to merge the output channels of the depthwise convolution to create new features. By doing so, the computational work needed to be done is less than the regular convolutional networks.

#### 5. In your own words, what is a bottleneck?
A bottleneck is the layer just before the output layer. The bottle neck has significantly fewer neurons than other layers serving as an information filter.

#### 6. How is a bottleneck different from the concept of layer freezing?
Layer freezing is a technique to control the way the weights are updated. Once a layer is frozen, the weights cannot be updated anymore. While layer freezing aims to accelerate training and to avoid overfitting, the goal of bottleneck layer is to "squeeze" important information out of the noisy data. 

#### 7. In the TF1 lab, you trained the last layer (all the previous layers retain their already-trained state). Explain how the lab used the previous layers (where did they come from? how were they used in the process?)
The previous layers are from a pre-trained neural network (Inception V3), with all the parmeters frozen. For each image, the TF1 lab script ran the frozen layers as the constant part of the network, calculate for each layer and saved the results in a bottleneck file. After generating the bottleneck files, the last layer training began. It randomly selected 10 images, fed in the model the bottleneck files and output the predictions. By comparing the predictions and actual lable, thelast layer's parameters were updated by backpropogation. 

#### 8. How does a low --learning_rate (step 7 of TF1) value (like 0.005) affect the precision? How much longer does training take?
The precision is increased. The training time is just slightly longer. 

#### 9. How about a --learning_rate (step 7 of TF1) of 1.0? Is the precision still good enough to produce a usable graph?
The precison is worse while the training time is similar. The precision is not stable enough to produce a usable graph.


#### 10. For step 8, you can use any images you like. Pictures of food, people, or animals work well. You can even use ImageNet images. How accurate was your model? Were you able to train it using a few images, or did you need a lot?


#### 11. Run the TF1 script on the CPU (see instructions above) How does the training time compare to the default network training (section 4)? Why?
It takes longer for training the default network on CPU. Because GPU has hundreds of simpler cores which can compute in parallel, training on GPU is much faster.

#### 12. Try the training again, but this time do export ARCHITECTURE="inception_v3" Are CPU and GPU training times different?
The training time on GPU is faster than that on CPU, especially when creating the bottleneck files.

#### 13. Given the hints under the notes section, if we trained Inception_v3, what do we need to pass to replace ??? below to the label_image script? Can we also glean the answer from examining TensorBoard?
```
python -m scripts.label_image --input_layer=Mul --input_height=299 --input_width=299  --graph=tf_files/retrained_graph.pb --image=tf_files/flower_photos/daisy/21652746_cc379e0eea_m.jpg
```

We can glean the answer from the "Graph" section on TensorBoard.
