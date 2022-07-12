###Transferlearning 
from tkinter.tix import Tree
from sklearn import datasets
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import os
import copy 
from torch.utils.data import DataLoader
from torchvision import datasets,models,transforms
import time
from torch.optim import lr_scheduler

##hper paramaters 
learning_rate = 0.01
## importing the data 
data_path = '/home/iamismail/Rebirth Pytorch/Dayfour/hymenoptera_data'
sets = ['train','val']
mean = np.array([0.5, 0.5, 0.5])
std = np.array([0.25, 0.25, 0.25])

data_transforms ={
     'train' : transforms.Compose([
         transforms.RandomResizedCrop(224),
         transforms.RandomHorizontalFlip(),
         transforms.ToTensor(),
         transforms.Normalize(mean,std)
     ]),
     'val' :transforms.Compose([
         transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
        transforms.Normalize(mean, std)
     ])
}

image_datasets = {x: datasets.ImageFolder(os.path.join(data_path, x),
                                          data_transforms[x])
                  for x in ['train', 'val']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                             shuffle=True, num_workers=0)
                                             for x in ['train', 'val']}

class_names = image_datasets['train'].classes

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(class_names)

 

def train_model(model, criterion, optimizer ,scheduler,num_epochs):
    best_model_copy = copy.deepcopy(model.state_dict())
    best_acc = 0.0 

    ##training the model 
    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        ## each epoch has a training and validaiton epoch 
        for phase in ['train','val']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss =0.0
            running_corrects = 0 

            ##iteration over the data 

            for images, labels in dataloaders[phase]:
                images = images.to(device)
                labels = labels.to(device)

                ##forward 
                ##track history 

                with torch.set_grad_enabled(phase =='train'):
                    outputs = model(images)
                    _,pred = torch.max(outputs, 1)
                    loss = criterion(outputs,labels)


                    ##backward 

                    if phase =='train':
                        optimizer.zero_grad()
                        loss.backward()
                        optimizer.step()
             # statistics
                running_loss += loss.item() * images.size(0)
                running_corrects += torch.sum(pred == labels.data)
            if phase == 'train':
                scheduler.step()

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            # deep copy the model
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

        print()
    time_elapsed = time.time()  
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model


model = models.resnet18(pretrained=True)
 
num_features = model.fc.in_features

## we have output of 2 clases 
model.fc = nn.Linear(num_features,2 )
model.to(device)
##respectively we can say nn.linear(num_features,)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),lr = learning_rate)

##schedular 
## updating the learning rate 
##this means in every 7 epochs of our learning rate will be multiplied gamma which is 0.1
step_lr_schedular = lr_scheduler.StepLR(optimizer, step_size=7 , gamma=0.1)


##training 
model = train_model(model , criterion,optimizer,step_lr_schedular,num_epochs=10) 

model_fr = models.resnet18(pretrained=True)
for param in model_fr.parameters():
    param.requires_grad = False
num_features = model_fr.fc.in_features

## we have output of 2 clases 
model_fr.fc = nn.Linear(num_features,2 )
model_fr.to(device)

criterion = nn.CrossEntropyLoss()
optimzer = torch.optim.SGD(model_fr.parameters(),lr = learning_rate)

##schedular 
step_lr_m_schedular = lr_scheduler.StepLR(optimizer,step_size=7,gamma=0.1)
model = train_model(model_fr,criterion,optimizer,step_lr_m_schedular,num_epochs=10 )