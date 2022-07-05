##Data Transforms 
import torch 
from torch.utils.data import Dataset
import numpy as np 


class WineDatast(Dataset):
     ## adding transform 
    def __init__(self,transform=None) :
        ### data louding 
        data = np.loadtxt('/home/iamismail/Rebirth Pytorch/Day two/data/wine/wine.csv',delimiter=",",dtype=np.float32,skiprows=1)
        self.x = data[:,1:]
        self.y =  data[:,[0]]  #n_samples = 1
        self.transform = transform
    def __getitem__(self, index):
        ##dataset[withindex]
        sample= self.x[index],self.y[index]

        if self.transform :
            sample = self.transform(sample)
        return sample

    def __len__(self):
        return self.n_samples
##tensor transform 
class toTensor:
    def __call__(self, sample):
        inputs ,labels = sample
        return torch.from_numpy(inputs),torch.from_numpy(labels)

##Multiplication transform        
class Multransform :
    def __init__(self,factor) :
        self.factor = factor

    def __call__(self, sample):
        inputs, target = sample
        inputs *= self.factor
        return inputs , target

           

##Applying the dataset 
dataset = WineDatast(transform=toTensor())
features, target = dataset[0]
print(type(features),type(target))

 