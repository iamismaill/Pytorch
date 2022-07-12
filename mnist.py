###Handwritten digits with pytorch 
from multiprocessing import allow_connection_pickling
from turtle import down
import torch 
import torch.nn as nn 
import torchvision
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt 
import numpy as np 
import torch.nn.functional as fn

##hperparamters 
Epochs = 10 
batch_size = 64

##transofrms 
transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])
##Loud and preprocessing Data 

train_set = torchvision.datasets.MNIST(root ='/Users/ismail/Desktop/Pytorchtutorails/',
train=True,download=True ,transform=transforms)

test_set = torchvision.datasets.MNIST(root ='/Users/ismail/Desktop/Pytorchtutorails/',
train =False,download=True,transform=transforms)

train_louder= DataLoader(train_set,batch_size=batch_size)
test_louder = DataLoader(test_set,batch_size=batch_size)


##Preporcessing Data
image, _ = train_set[0] 
print(image.size())
image_flatten = image.view(image.shape[0], -1)
print (image_flatten.size())
torch.Size([1, 28, 28]) 
torch.Size([1, 784])

##Our model 
my_model= torch.nn.Sequential(            
         torch.nn.Linear(784,10),
         torch.nn.Sigmoid(), 
         torch.nn.Linear(10,10), 
         torch.nn.LogSoftmax(dim=1) 
         )



##defining optimizer and loss function
### Since i am  with a multi-class classification problem, I chose cross-entropy as My Loss function. so I use negative log-likelihood nn.NLLLoss () that combines with the softmax nn.LogSoftmax


learning_rate = 0.01
criterion = torch.nn.NLLLoss()
optimizer = torch.optim.SGD(my_model.parameters(),lr=learning_rate)


##Training the model 
for e in range(Epochs):
      running_loss = 0
      for images,labels in  train_louder:
          images = images.view(images.shape[0], -1)
          output = my_model(images)
          loss = criterion(output,labels)
          loss.backward()
          optimizer.step()
          optimizer.zero_grad()
          running_loss += loss.item()
          
      print("Epochs {} - Training Loss :{}".format(e,
        running_loss/len(train_louder))) 

## Evaluting the model 
##let's see how well our model was generalized by applying it on a test datast 

correct_count, all_count = 0, 0
for images,labels in test_louder:
  for i in range(len(labels)):
    img = images[i].view(1, 784)
    logps = my_model (img)
    ps = torch.exp(logps)
    probab = list(ps.detach().numpy()[0])
    pred_label = probab.index(max(probab))
    true_label = labels.numpy()[i]
    if(true_label == pred_label):
      correct_count += 1
    all_count += 1
print("\nAccuracy of the model is",(correct_count/all_count))