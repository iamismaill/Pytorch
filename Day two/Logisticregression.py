
## Logist Regression - Pytorch 

## Design model ( input , output, forward pass )
## Construct loss and optimizer 
## Train the model 
   ###  Forward pass - compute predictions 
   ## backward pass - compute gradients 
   ## update weights 


from re import L
import torch 
import numpy as np 
import torch.nn as nn 
from sklearn import datasets 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

##Step zero 
   ## preparing the data 
data = datasets.load_breast_cancer()
### this data binary classifiation problem , we will predict cancer based on input features
X, y = data.data, data.target 
n_samples , n_features = X.shape 
print(n_samples, n_features)

## spliting the data 
X_train , X_test , y_train ,y_test = train_test_split(X,y,test_size=0.2 , random_state=1234)


##Scale
scaler = StandardScaler()
X_train =scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

##converting to torch tensor 
X_train = torch.from_numpy(X_train.astype(np.float32))
X_test =  torch.from_numpy(X_test.astype(np.float32))
y_train = torch.from_numpy(y_train.astype(np.float32))
y_test = torch.from_numpy(y_test.astype(np.float32))

##reshaping y_train & y_test 
 
y_train = y_train.view(y_train.shape[0],1)
y_test = y_test.view(y_test.shape[0],1)
## 1.model 
## f= wx+b , at the end we will apply sigmoid function 

class Logisticregrssoin(nn.Module):

    def __init__(self,n_input_features) :
        super(Logisticregrssoin,self).__init__()

        ##layer 
        self.linear = nn.Linear(n_input_features,1)
    def forward(self,x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

model = Logisticregrssoin(n_features)
## 2.los and optimizer 
criterion = nn.BCELoss()
## passing paramaters we need to optimize 
optimizer = torch.optim.SGD(model.parameters(),lr= 0.01)
##3. training loop 
n_iteration = 100 

##training loop 
for epochs in range(n_iteration):
    ##forward pass and loss 
    y_prediction = model(X_train)
    
    loss = criterion(y_prediction,y_train)

    ##backward pass ( calculate the gradients )
    loss.backward()

    ##update the weights 
    optimizer.step()

    ##empty the gradients 
    optimizer.zero_grad()

    if epochs % 10 == 0:
        print(f"epoch {epochs+1}, loss : {loss.item():4f}")


### Evaluation of our model 


with torch.no_grad():
    y_predicted = model(X_test)
    ##Converting this class labels (0/1)
    y_predicted_classes = y_predicted.round()
    acc = y_predicted_classes.eq(y_test).sum()/ float(y_test.shape[0])
    print(f"Acuracy:  {acc:4f}")