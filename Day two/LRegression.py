from random import random
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib
from tqdm import tqdm
import torch
import torch.nn as nn

matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
sns.set_style("darkgrid")

from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

separable = False
while not separable:
    samples = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1, flip_y=-1)
    red = samples[0][samples[1] == 0]
    blue = samples[0][samples[1] == 1]
    separable = any([red[:, k].max() < blue[:, k].min() or red[:, k].min() > blue[:, k].max() for k in range(2)])


red_labels = np.zeros(len(red))
blue_labels = np.ones(len(blue))

y = np.append(red_labels,blue_labels)
X = np.concatenate((red,blue),axis=0)


##Step one splitting the dataset 
X_train , X_test , y_train , y_test = train_test_split(X,y, train_size=0.33, random_state=1234)
X_train, X_test = torch.Tensor(X_train),torch.Tensor(X_test)
y_train, y_test = torch.Tensor(y_train),torch.Tensor(y_test)
n_features, n_samples = X_train.shape
# Step two :Model class

class Logisticregression(torch.nn.Module):
    def __init__(self,n_input_features) :
        super(Logisticregression,self).__init__()
        self.linear = nn.Linear(n_input_features,1)

    def forward(self, x):
        output = torch.sigmoid(self.linear(x))
        return output

model = Logisticregression(n_features)

##loss and optimizers 
loss = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(),lr = 0.01)

##training the model 
n_iteration = 2000

for epochs in range(n_iteration):
    ##forward pass 
    y_predicton = model(X_train)
    ##loss
    loss = loss(y_predicton,y_train)

    loss.backward()

    ##  ##update the weights 
    optimizer.step()

    ##zero grade 
    optimizer.zero_grad()

    

