
import numpy as np #the funny statment 
from PIL import Image
import cv2
import os
#for saving the numpy array as a csv
import pandas as pd


def convertImagesToNpy(directory, outputPath):
    count=0
    imageList= os.listdir(directory)
    assert len(imageList)>0, "Images not loaded in correctly"

    for current in imageList:
        img = cv2.imread(os.path.join(directory, current))
        img = img.astype(np.float32) / 255.0  # [0, 255] ==> [0, 1]
        img = img ** 2.2
        img = img[...,::-1] # BGR ==> RGB
        img = img.astype(np.float16)

        print(directory+current)
        np.save(os.path.join(outputPath, "image_%d.npy" % count), img)

        count+=1

def convertBasisToNpy(directory, outputPath, renderMode):
    count=0
    imageList= os.listdir(directory)
    assert len(imageList)>0, "Images not loaded in correctly"

    for current in imageList:
        img = cv2.imread(os.path.join(directory, current))
        img = img.astype(np.float32) / 255.0  # [0, 255] ==> [0, 1]
        img = img ** 2.2
        img = img[...,::-1] # BGR ==> RGB
        img = img.astype(np.float16)

        print(directory+current)
        np.save(os.path.join(outputPath, "basis%d_%d.npy" % (renderMode, count)), img)

        count+=1

def convertUVToNpy(directory, outputPath):
    count=0
    imageList= os.listdir(directory)
    assert len(imageList)>0, "Images not loaded in correctly"

    for current in imageList:
        img = cv2.imread(os.path.join(directory, current))
        img = img.astype(np.float32) / 255.0  # [0, 255] ==> [0, 1]
        img = img ** 2.2
        img = img[...,::-1] # BGR ==> RGB

        print(directory+current)
        np.save(os.path.join(outputPath, "uv_%d.npy" % count), img)

        count+=1

def convertMaskToGray(directory, outputPath):
    count=0
    imageList= os.listdir(directory)
    assert len(imageList)>0, "Images not loaded in correctly"

    for current in imageList:
        img = cv2.imread(os.path.join(directory, current))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #img = img.astype(np.uint8)

        print(directory+'_'+current)
        cv2.imwrite(os.path.join(outputPath, "mask_%d.png" % count), img)

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

directory = "new_data/kuan-yu/output/IBRelight_UV/"
outputPath = "new_data/kuan-yu/output/UV/"
#convertUVToNpy(directory, outputPath)

directory = "new_data/kuan-yu/output/mask_RGB/"
outputPath = "new_data/kuan-yu/output/mask/"
convertMaskToGray(directory, outputPath)