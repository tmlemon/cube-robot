"""
Created Wed Dec 19 09:56:52 2018
@author: tlemon
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


flatten = lambda lst: [item for sublist in lst for item in sublist]

im = Image.open('cube.jpg')
size = im.size
pix = im.load()

pixMap = []
for i in range(0,size[1],40):
    hold = []
    for j in range(0,size[0],40):
        p = pix[j,i]
        pixMap.append(p)
pixMap = np.array(pixMap)


tl = pixMap[0:int(len(pixMap[0])/3)+1,0:int(len(pixMap)/3)+1]
ml = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,0:int(len(pixMap)/3)+1]
bl = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,0:int(len(pixMap)/3)+1]

tm = pixMap[0:int(len(pixMap[0])/3)+1,int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]
mm = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]
bm = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]

tr = pixMap[0:int(len(pixMap[0])/3)+1,2*int(len(pixMap)/3)+1:int(len(pixMap))+1]
mr = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,2*int(len(pixMap)/3)+1:int(len(pixMap))+1]
br = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,2*int(len(pixMap)/3)+1:int(len(pixMap))+1]

