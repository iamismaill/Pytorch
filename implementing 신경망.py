#### 신경망 구현하기 



## 간단한 분료 모델 구현하기 

## here i will implement simple model that performs classification 
## required libraries 
from cProfile import label
from doctest import OutputChecker
from tkinter.tix import InputOnly
import numpy as np 
import torch 
import torch.nn as nn
from sklearn.datasets import make_blobs
import torch.nn.functional as fn 
import matplotlib.pyplot as plt

### Sample dataset 
## we will create NN that can predict only two classes 
x_train, y_train = make_blobs(n_samples=80, n_features=2, centers=[[1,1],[-1,-1],[1,-1],[-1,1]], shuffle=True, cluster_std=0.3)
x_test, y_test = make_blobs(n_samples=20, n_features=2, centers=[[1,1],[-1,-1],[1,-1],[-1,1]], shuffle=True, cluster_std=0.3)


## let's create dataset to put our model 

def label_map (y_,from_,to_):
    y =np.copy(y_)
    for f in from_:
        y[y_ ==f] =to_
    return y 
## so basicaly there are 80개  two dimensional (2차원) data in the training dataset (학습 데이터셋) and 20 in the expiremental dataset (실험 데이터셋)
###and there are four clusters meach marked 0,1,2,3
y_train = label_map(y_train,[0,1],0)
y_train = label_map(y_train,[2,3],1)
y_test = label_map(y_test,[0,1],0)
y_test = label_map(y_test,[2,3],1)

## here label_map() 합수 merges functions with labels 0 or 1 into label 0 and merges data with labels 2 and 3 into 1 

## let's visualize the data 

def vis_data(x,y = None, c = 'r'):
    if y is None:
        y = [None] * len(x)
    for x_, y_ in zip(x,y):
        if y_ is None:
            plt.plot(x_[0], x_[1], '*',markerfacecolor='none', markeredgecolor=c)
        else:
            plt.plot(x_[0], x_[1], c+'o' if y_ == 0 else c+'+')

plt.figure()
vis_data(x_train, y_train, c='r')
###plt.show()


##our vis_data () 함수 can visually check whether the data is properly created and labeled 


## Implement NN Model 

class NN(torch.nn.Module):
    def __init__(self,input_size, hidden_layer) :
        super(NN,self).__init__()
        ## layers
        self.input_size = input_size
        self.hidden_layer = hidden_layer
        self.linear_1 = nn.Linear(self.input_size, self.hidden_layer)
        ##our relu function will return 0 if the input values is less then 0 and return 1 if the input is greater 0
        self.relu = nn.ReLU()
        self.linear_2 = nn.Linear(self.hidden_layer,1)
        ## sigmoid function will return arandom number between 0 and 1 
        self.sigmoid = nn.Sigmoid()


## forward function 
    def forward ( self,input_layer ):
        linear1 = self.linear_1(input_layer)
        relu = self.relu(linear1)
        linear2 = self.linear_2(relu )
        output = self.sigmoid(linear2)

        return output

###테이터셋 파이토치 텐서를 변환 
#x_train = torch.from_numpy(x_train.astype(np.float32))
#x_test = torch.from_numpy(x_test.astype(np.float32))
#y_train = torch.from_numpy(y_train.astype(np.float32))
#y_test = torch.from_numpy(y_test.astype(np.float32))
x_train = torch.FloatTensor(x_train)
x_test = torch.FloatTensor(x_test)
y_train = torch.FloatTensor(y_train)
y_test = torch.FloatTensor(y_test)
## let's create our model   
model = NN(2,5)
##hperparamaters 
learning_rate = 0.01
criterion = nn.BCELoss()
epochs = 100 
optimizer = torch.optim.SGD(model.parameters(),lr = learning_rate)

## for loop training 

for epoch in range(epochs):

    ##forward 
    output = model(x_train)
    
    ##reshape y_train 
    y_train = y_train.view(y_train.shape[0],1)
    y_test = y_test.view(y_test.shape[0],1)
   

    ## loss 
    loss = criterion(output,y_train)
    ##backward 
    loss.backward()
    ## Optimizer 
    optimizer.step()
    ## update our paramters 
    optimizer.zero_grad()
    if epoch %10  == 0:
        print(f"epoch {epochs+1}, loss : {loss:3f}")



