# -*- coding: utf-8 -*-

import numpy as np #the funny statment 
from PIL import Image
import os
#for saving the numpy array as a csv
import pandas as pd

directory = "new_data/kuan-yu/subset/"
outputPath = "new_data/kuan-yu/output/"

imageList= os.listdir(directory)
assert len(imageList)>0, "Images not loaded in correctly"

for current in imageList:
    if current.endswith(".jpg") or current.endswith(".png"):
        # convert the image to numpy array
        print(directory+current)
        a= Image.open(directory+ current)
        data= np.array(a)
        data.tofile(outputPath+'data.csv',sep=', ')
       # df= pd.DataFrame(data)
       # pd.DataFrame(data).to_csv(outputPath+"test.csv") #the output 
   









