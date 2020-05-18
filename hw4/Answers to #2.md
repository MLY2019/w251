### Name all the layers in the network, describe what they do.
1. The 1st layer declares the input size 24x24.
2. The 2nd layer performes convolution with 8 kernels with the size of 5x5 at the stride of 1. The input is padded by 2 pixles at all sides and the ReLu function is used as the activation function. The 4th layer bascically does the same with the only difference in that it uses more kernels for convolution -- 16 instead of 8. 
3. The 3rd layer performes max pooling with the size of 2x2 at the stride of 2. The 5th layer performes max pooling with the size of 3x3 at the stride of 3.
5. The 6th layer uses the function of Softmax to turn logits into probabilities for each class. 

### Experiment with the number and size of filters in each layer. Does it improve the accuracy?

### Remove the pooling layers. Does it impact the accuracy?

### Add one more conv layer. Does it help with accuracy?

### Increase the batch size. What impact does it have?

### What is the best accuracy you can achieve? Are you over 99%? 99.5%?
