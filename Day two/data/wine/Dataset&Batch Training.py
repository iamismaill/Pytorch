###Dataset and DataLoader - Batch Training  

import enum
import numpy as np
import torch 
from torch.utils.data import Dataset , DataLoader
import math



class WineDataset(Dataset) :

    def __init__(self) :
        ### data louding 
        data = np.loadtxt('/home/iamismail/Rebirth Pytorch/Day two/data/wine/wine.csv',delimiter=",",dtype=np.float32,skiprows=1)
        self.x = torch.from_numpy(data[:,1:])
        self.y =  torch.from_numpy(data[:,[0]])  #n_samples = 1
        self.n_samples = data.shape[0]




    def __getitem__(self, index):
        ##dataset[withindex]
        return self.x[index],self.y[index]
    def __len__(self):
        return self.n_samples


dataset = WineDataset()
datalouder = DataLoader(dataset=dataset,batch_size=4 , shuffle=True,num_workers=2)

dataiter = iter(datalouder)
data = dataiter.next()
features ,labels = data
 


## training loop 
n_epchs = 2 
total_sample = len(dataset)
n_iteratoin = math.ceil(total_sample/4)
print(total_sample)
print(n_iteratoin)

for epochs in range(n_epchs):
    for i , (inputs, labels) in enumerate(datalouder):
        ##forward , backward and upate 
        if (i*1) %5 ==0 :
            print(f"epochs :{epochs +1}/ {n_epchs},step {i+1} /{n_iteratoin}, inputs ={inputs.shape} ")
     