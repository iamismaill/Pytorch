###Model loud & Saving 
import torch 
import torch.nn as nn 
### 
Path = ""
##torch.save(arg,Path)
##torch save we can use tensor models or any dictionary as paramaters for saving , in here the result is serialized and not human readable 

##Saving our model 

##Option one : The lazy one 
## torch.save (model,path )

##louding the model 
## model = torch.load(Path)
##model.eval()
##torch.loud(path)


##Option two :
## State Dict : will hold the paramters 
###torch.save(model.state_dict() , path )

##later if we want to load our model ,model must be created again with paramtes 
##model = Model(*args,**kwargs)
##model.load_state_dict(torch.load(Path))
##model.eval()


