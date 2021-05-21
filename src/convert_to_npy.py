
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

def convertBasisToNpy(directory, outputPath, renderMode):
    count=0
    imageList= os.listdir(directory)
    assert len(imageList)>0, "Images not loaded in correctly"

    for current in imageList:
        print(directory+current)
        a= Image.open(directory+ current)
        data= np.array(a)
        path= outputPath+ 'basis'+str(renderMode)+'_'+str(count)+'.npy'
        data.tofile(str(path),sep=', ')
        count+=1

def convertUVToNpy(directory, outputPath):
    count=0
    imageList= os.listdir(directory)
    assert len(imageList)>0, "Images not loaded in correctly"

    for current in imageList:
        print(directory+current)
        a= Image.open(directory+ current)
        data= np.array(a)
        path= outputPath+ 'uv_'+str(count)+'.npy'
        data.tofile(str(path),sep=', ')
        count+=1


directory = "new_data/kuan-yu/2048/"
outputPath = "new_data/kuan-yu/output/image/"
#convertImagesToNpy(directory,outputPath)

directory = "new_data/kuan-yu/blender/lambert/"
outputPath = "new_data/kuan-yu/output/basis/"
#convertBasisToNpy(directory, outputPath, 0)

directory = "new_data/kuan-yu/blender/ct_02/"
outputPath = "new_data/kuan-yu/output/basis/"
#convertBasisToNpy(directory, outputPath, 1)

directory = "new_data/kuan-yu/blender/ct_05/"
outputPath = "new_data/kuan-yu/output/basis/"
#convertBasisToNpy(directory, outputPath, 2)

directory = "new_data/kuan-yu/blender/ct_13/"
outputPath = "new_data/kuan-yu/output/basis/"
#convertBasisToNpy(directory, outputPath, 3)

directory = "new_data/kuan-yu/blender/ct_34/"
outputPath = "new_data/kuan-yu/output/basis/"
#convertBasisToNpy(directory, outputPath, 4)

directory = "new_data/kuan-yu/output/IBRelight"
outputPath = "new_data/kuan-yu/output/UV/"
convertBasisToNpy(directory, outputPath)