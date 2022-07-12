## we will take these steps 
  ## Datalouder ,Transformations
  ##Multi layer neural net ,activatoin function 
  ## loss and optimizer 
  ## Training loop (we will use batch training)
  ## Model Evalution 
  ### at the end we will try if our code can support GPU

##
import torch 
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import torchvision.transforms as transforms  
import torchvision
from torch.utils.tensorboard import SummaryWriter
 

writer = SummaryWriter("runs/mnist")
##hyper paramaters 
input_size = 784 
hidden_size = 100
num_classes = 10 
num_epochs = 20
batch_size = 100 
learning_rate = 0.001

##data louding 
train_data = torchvision.datasets.MNIST(root='/Users/ismail/Pytorchtutorails',train=True , transform=transforms.ToTensor() ,download=True)
test_data = torchvision.datasets.MNIST(root='/Users/ismail/Pytorchtutorails',train=False, transform= transforms.ToTensor())

##data louders 
train_louder = torch.utils.data.DataLoader(dataset=train_data,batch_size=batch_size, shuffle=True)
test_louder = torch.utils.data.DataLoader(dataset=test_data,batch_size=batch_size,shuffle=False)

##looking one batch of our dat 
examples = iter(train_louder)
samples ,labels = examples.next()
print(samples.shape)
print(labels.shape)


import sys
for i in range(6) :
    plt.subplot(2,3,i+1) 
    plt.imshow(samples[i][0])
img_grid = torchvision.utils.make_grid(samples)
writer.add_image("mnist images",img_grid)
writer.close()
import sys 
##ys.exit()

##our goal is to classify these images into 10 digits , so we will setup fully connected neural network with one hidden layer

##our goal is to classify these images into 10 digits , so we will setup fully connected neural network with one hidden layer

class Neuralnetwork(nn.Module):
    def __init__(self, input_size, hidden_size,num_classes):
        super(Neuralnetwork,self).__init__()

        ##our layers 
        self.layer1 = nn.Linear(input_size,hidden_size)
        self.relu = nn.ReLU()
        self.layer2 =nn.Linear(hidden_size,num_classes)
    def forward(self,x):
        output = self.layer1(x)
        output = self.relu(output)
        output = self.layer2(output)

        return output

model = Neuralnetwork(input_size=input_size,hidden_size=hidden_size,num_classes=num_classes)

##loss and optimzier 
criterian = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr =learning_rate)


##Training loop 
n_total_steps = len(train_data)
running_loss = 0.0
running_correct =0.0
for epochs in range(num_epochs):
    for i, (images,labels) in enumerate(train_louder):

        ### our image shape is 100,1,28 ,28 so we need to reshape coz our inputsize is 784 so it should be (100 ,784)
        images = images.reshape(-1,28*28)
         
    #forward 
    outputs = model(images)
    loss = criterian(outputs,labels)
    ## backward 
    optimizer.zero_grad()
    loss.backward()

    ##update paramaters 
    optimizer.step()

    ##printing the loss
    running_loss += loss.item()
    _,predicted = torch.max(outputs.data,1)
    running_correct += (predicted == labels).sum().item()

    if (i+1) %100 ==0 :
        print(f"epochs {epochs +1} /{num_epochs},step :{i+1} /{n_total_steps} loss :{loss.item():4f}")
        ##calculating mean value and adding tensorboard 
        writer.add_scalar("training loss", running_loss /100,epochs * n_total_steps + i)
        writer.add_scalar("accuracy", running_correct /100,epochs * n_total_steps + i)
        running_correct =0
        running_loss = 0.0

    ##loss 
    
    ##gradient 

with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_louder:
        images = images.reshape(-1, 28*28)
        labels = labels
        outputs = model(images)
        # max returns (value ,index)
        _, predicted = torch.max(outputs.data, 1)
        n_samples += labels.size(0)
        n_correct += (predicted == labels).sum().item()

    acc = 100.0 * n_correct / n_samples
    print(f'Accuracy of the network on the 10000 test images: {acc} %')