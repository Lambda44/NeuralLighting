
import numpy as np #the funny statment 
from PIL import Image
import os
#for saving the numpy array as a csv
import pandas as pd


def convertImagesToNpy(directory, outputPath):
    count=0
    imageList= os.listdir(directory)
    assert len(imageList)>0, "Images not loaded in correctly"

    for current in imageList:
        print(directory+current)
        a= Image.open(directory+ current)
        data= np.array(a)
        path= outputPath+ 'image_'+str(count)+'.npy'
        data.tofile(str(path),sep=', ')
        count+=1




directory = "new_data/kuan-yu/2048/"
outputPath = "new_data/kuan-yu/output/"
convertImagesToNpy(directory,outputPath)












