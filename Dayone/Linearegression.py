##Three steps 
##1.Define the model (input , outputsize,forward)
##2.Constrcut the loss and optimzer 
##3.Training loop 
   ## forward pass : compute prediction 
   ## backward pas :gradient 
   ## update the weights 

import torch 
import torch.nn as nn 
import numpy as np 
from sklearn import datasets
import matplotlib.pyplot as plt 

## preparing the data 
X_numpy , y_numpy = datasets.make_regression(n_samples=100, n_features=1,noise=20 , random_state=1)

#convert to tensor 
X = torch.from_numpy(X_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))
print(y.shape)
#reshape y 
y = y.view(y.shape[0],1)
print(y.shape)

n_samples , n_features = X.shape
input_size = n_features
output_size = 1
##lr model 
model = nn.Linear(input_size,output_size)

## Construct the loss and optimizer 
learng_rate = 0.01
loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=learng_rate)

##before training 
##print(f"Prediction before training f(5):{model(")
## training loop 
n_iteration = 100

for epchos in range(n_iteration):


    ##forwad pass 
    y_pred = model(X)

    ##loss
    ls = loss(y_pred,y)

    #gradient 
    ls.backward()

    ##update weights 
    optimizer.step()
    ##zero grad
    optimizer.zero_grad()
    print(f"epochs {epchos},loss:{ls.item()}")

## plot 

prediction = model(X).detach()
plt.plot(X_numpy,y_numpy,'ro')
plt.plot(X_numpy,prediction,'b') 
plt.show()

### safasfasfafgfgggsafsa  