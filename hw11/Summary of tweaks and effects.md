The most effective changes I made are those on the two hidden layers of the model:

1. Increase the number of neurons to 256 and 128, respectively;

2. Add the initialization method of ```lecun_uniform```; 

3. Add l2 regularization of 0.001;

4. Implement Batch Normalization.

All the above changes made the model performed better and learning converged faster.

I also tested the initialzaition method of ```xaiver``` but it didn't improve the model performance as much as ```lecun_uniform``` did. 

The other changes also found effective include increase the training epoch to 20 and increase the batch size to 50. 

I tried using ```adamax``` instead of ```adam``` as the optimizer but found it degraded the model.

Based on my observations, the hidden layers' parameters are critical to the model performance and if time allows, we should extensively test different values and combinations on those parameters.  

