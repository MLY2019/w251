#### How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
It took around 25 hrs to run for 50,000 steps on the dual p100 VMs.

#### Do you think your model is fully trained? How can you tell?
I don't think the model is fully trained as the train loss still trended on decrease when training finished.

#### Were you overfitting?
No, because the evaluation loss still trended on decrease when training finished. 

#### Were your GPUs fully utilized?
Yes.

#### Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?
Yes, I monitored network traffic using command nmon. Yes, network was the bottleneck.

#### Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?
In the config file, transformer's learning rate policy was used and it means that learning rate is to increase to a max value (hat) and then decay. The warm up steps was set to 8,000 so in the plot the learning rate rose to close to 1e-3 in 8,000 steps and then decayed as training proceeded.

#### How big was your training set (mb)? How many training lines did it contain?
The training set contained two files: 
train.clean.de, 695MB, 4524868 lines;
train.clean.en, 622MB, 4524868 lines.

#### What are the files that a TF checkpoint is comprised of?
A TF checkpoint is comprised of three files:
meta file: it stores the saved TF graph structure;
index file: it stores the list of saved variables and shapes;
data file: it stores the values of all saved variables.

#### How big is your resulting model checkpoint (mb)?
With all three file, it is around 742MB.

#### Remember the definition of a "step". How long did an average step take?
With one batch of training data passed to the model and weights updated, training completes one step. The average time per step was 1.816s.

#### How does that correlate with the observed network utilization between nodes?
With distributed training on two VMs, information exchange between nodes is necessary to update weights. Therefore, the training speed is limited by the network utilization between nodes.
