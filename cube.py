"""
Created Wed Dec 19 09:56:52 2018
@author: tlemon
"""
from PIL import Image
import numpy as np

def dist(pt,ref):
    r1,g1,b1 = pt
    r2,g2,b2 = ref
    d = np.sqrt((r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2)
    return d
    

im = Image.open('cube.jpg')
size = im.size
pix = im.load()

skip = 100

pixMap = []
for i in range(0,size[1],skip):
    hold = []
    for j in range(0,size[0],skip):
        p = pix[j,i]
        hold.append(p)
    pixMap.append(hold)
pixMap = np.array(pixMap)


tl = pixMap[0:int(len(pixMap[0])/3)+1,0:int(len(pixMap)/3)+1]
tm = pixMap[0:int(len(pixMap[0])/3)+1,\
    int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]
tr = pixMap[0:int(len(pixMap[0])/3)+1,\
    2*int(len(pixMap)/3)+1:int(len(pixMap))+1]
    
ml = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,\
    0:int(len(pixMap)/3)+1]
mm = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,\
    int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]
mr = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,\
    2*int(len(pixMap)/3)+1:int(len(pixMap))+1]

bl = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,\
    0:int(len(pixMap)/3)+1]
bm = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,\
    int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]
br = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,\
    2*int(len(pixMap)/3)+1:int(len(pixMap))+1]

squares = [[tl,tm,tr],[ml,mm,mr],[bl,bm,br]]


refColors = [['W',[255,255,255]],['Y',[255,255,0]],['O',[255,128,0]],\
        ['R',[255,0,0]],['G',[0,255,0]],['B',[0,0,255]]]

txtColors = []
for row in squares:
    hold = []    
    for sq in row:
        rMean = gMean = bMean = count = 0
        for line in sq:
            for item in line:
                rMean += item[0]
                gMean += item[1]
                bMean += item[2]
                count += 1
        rMean,gMean,bMean = rMean/count,gMean/count,bMean/count
        closestRef = []
        for ref in refColors:
            closestRef.append(dist([rMean,gMean,bMean],ref[1]))
        match = closestRef.index(min(closestRef))
        hold.append(refColors[match][0])
    txtColors.append(hold)
txtColors = np.array(txtColors)

print(txtColors)