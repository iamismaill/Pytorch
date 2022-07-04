###Dataset and DataLoader - Batch Training  

import numpy as np
import torch 
from torch.utils.data import Dataset , DataLoader


class WineDataset(Dataset) :

    def __init__(self) :
        ### data louding 
        data = np.loadtxt('/home/iamismail/Rebirth Pytorch/Day two/data/wine/wine.csv',delimiter=",",dtype=np.float32,skiprows=1)

    def __getitem__(self, index):
        ##dataset[withindex]

    def __len__(self):
        ##length of our dataset  

