from turtle import down
from sklearn.manifold import trustworthiness
from sklearn.utils import shuffle
import torch 
import matplotlib.pyplot as plt 

import torch.nn as nn 
import os 
import numpy as  np 
import torchvision
import torch.nn.functional as fn 
from torchvision.transforms import transforms
from torch.utils.data import DataLoader

batchsize = 64
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
##import the data 

train_set = torchvision.datasets.MNIST(root ='/home/iamismail/Rebirth Pytorch',train=True, download=True,transform=transforms.ToTensor() )
test_set = torchvision.datasets.MNIST(root='/home/iamismail/Rebirth Pytorch',train=False,download=True,transform=transforms.ToTensor())

##datasetlouder 
train_louder = DataLoader(train_set,batch_size=64,shuffle=False,num_workers=2)
test_louder = DataLoader(test_set,batch_size=64,shuffle=False,num_workers=2)


#Visualizing the iamges

def _image_show(img):
    np_image = img.numpy()
    plt.imshow(np.transpose(np_image, (1, 2, 0)))

dataiter = iter(train_louder)
image,labels = dataiter.next()

_image_show(torchvision.utils.make_grid(image))


##moderl paramaters
 
n_steps = 28 
n_inputs = 28
n_hidden = 150 
n_outputs = 10 
n_epochs = 10 


class RNNimageclasiffication(nn.Module):
    def __init__(self, batch_size,n_steps,n_inputs,n_hidden,n_outputs) -> None:
        super(RNNimageclasiffication,self).__init__()
        self.batch_size = batch_size
        self.n_stps = n_steps
        self.n_inputs = n_inputs
        self.n_hidden = n_hidden
        self.n_outputs = n_outputs

        self.basic_rnn = nn.RNN(self.n_inputs,self.n_hidden)
        self.Fc = nn.Linear(self.n_hidden,self.n_outputs)

    def init_hidden(self,):
        
        return (torch.zeros(1, self.batch_size, self.n_hidden))
    
    def forward(self,X):
        ## X to dimenstions(n_steps x batchsize x n_inputs)
        X = X.permute(1,0,2)
        self.batch_size = X.size(1)
        self.hidden = self.init_hidden()
        
        lstm_out, self.hidden = self.basic_rnn(X, self.hidden)      
        out = self.Fc(self.hidden)
        
        return out.view(-1, self.n_outputs) 


##taining 
model =RNNimageclasiffication(batchsize,n_steps,n_inputs,n_hidden,n_outputs)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr = 0.001)


def get_accuracy(logit, target, batch_size):
    corrects = (torch.max(logit, 1)[1].view(target.size()).data == target.data).sum()
    accuracy = 100.0 * corrects/batch_size
    return accuracy.item()


for epoch in range(n_epochs):
    training_running_loss= 0.0
    train_acc = 0.0
    model.train()


    for i , data in enumerate(train_louder):
        optimizer.zero_grad()

        model.hidden = model.init_hidden()
        inputs,labels = data 
        inputs = inputs.view(-1,28,28)

        outputs = model (inputs)

        loss =criterion(outputs,labels)
        loss.backward()
        optimizer.step()

        training_running_loss += loss.detach().item()
        train_acc += get_accuracy(outputs, labels, batchsize)
    model.eval()
    print('Epoch:  %d | Loss: %.4f | Train Accuracy: %.2f' 
          %(epoch, training_running_loss / i, train_acc/i))


##computing accuracty on test set 
test_acc = 0.0
for i, data in enumerate(test_louder, 0):
    inputs, labels = data
    inputs = inputs.view(-1, 28, 28)

    outputs = model(inputs)

    test_acc += get_accuracy(outputs, labels, batchsize)
        
print('Test Accuracy: %.2f'%( test_acc/i))