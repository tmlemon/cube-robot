"""
Created Wed Dec 19 09:56:52 2018
@author: tlemon
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def dist(pt,ref):
    r1,g1,b1 = pt
    r2,g2,b2 = ref
    d = np.sqrt((r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2)
    return d
    

im = Image.open('cube.jpg')
size = im.size
pix = im.load()

pixMap = []
for i in range(0,size[1],20):
    hold = []
    for j in range(0,size[0],20):
        p = pix[j,i]
        hold.append(p)
    pixMap.append(hold)
pixMap = np.array(pixMap)


tl = pixMap[0:int(len(pixMap[0])/3)+1,0:int(len(pixMap)/3)+1]
ml = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,\
    0:int(len(pixMap)/3)+1]
bl = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,\
    0:int(len(pixMap)/3)+1]

tm = pixMap[0:int(len(pixMap[0])/3)+1,\
    int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]
mm = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,\
    int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]
bm = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,\
    int(len(pixMap)/3)+1:2*int(len(pixMap)/3)+1]

tr = pixMap[0:int(len(pixMap[0])/3)+1,\
    2*int(len(pixMap)/3)+1:int(len(pixMap))+1]
mr = pixMap[int(len(pixMap[0])/3)+1:2*int(len(pixMap[0])/3)+1,\
    2*int(len(pixMap)/3)+1:int(len(pixMap))+1]
br = pixMap[2*int(len(pixMap[0])/3)+1:int(len(pixMap[0]))+1,\
    2*int(len(pixMap)/3)+1:int(len(pixMap))+1]

squares = [tl,ml,bl,tm,mm,bm,tr,mr,br]


sqCoord = [[0,2],[0,1],[0,0],[1,2],[1,1],[1,0],[2,2],[2,1],[2,0]]
refColors = [[255,255,255],[255,255,0],[255,128,0],[255,0,0],[0,255,0],\
    [0,0,255]]


for i,sq in enumerate(squares):
    rMean = gMean = bMean = count = 0
    for row in sq:
        for item in row:
            rMean += item[0]
            gMean += item[1]
            bMean += item[2]
            count += 1
    rMean,gMean,bMean = rMean/count,gMean/count,bMean/count
    closestRef = []
    for ref in refColors:
        closestRef.append(dist([rMean,gMean,bMean],ref))
    match = closestRef.index(min(closestRef))
    rgb = '#'+hex(refColors[match][0]).split('x')[-1].zfill(2)+\
        hex(refColors[match][1]).split('x')[-1].zfill(2)+\
        hex(refColors[match][2]).split('x')[-1].zfill(2)
    x,y = sqCoord[i][0],sqCoord[i][1]
    plt.scatter(x,y,color=rgb,s=2000,marker='s')
plt.show()
plt.close()

'''
for i,sq in enumerate(squares):
    rMean = gMean = bMean = count = 0
    for row in sq:
        for item in row:
            rMean += item[0]
            gMean += item[1]
            bMean += item[2]
            count += 1
    rMean,gMean,bMean = rMean/count,gMean/count,bMean/count
    closestRef = []
    for ref in refColors:
        closestRef.append(dist([rMean,gMean,bMean],ref))
    match = closestRef.index(min(closestRef))
    rgb = '#'+hex(refColors[match][0]).split('x')[-1].zfill(2)+\
        hex(refColors[match][1]).split('x')[-1].zfill(2)+\
        hex(refColors[match][2]).split('x')[-1].zfill(2)
    x,y = sqCoord[i][0],sqCoord[i][1]
    plt.scatter(x,y,color=rgb,s=2000,marker='s')
plt.show()
plt.close()
'''

for sq in squares:
    r,g,b = [],[],[]
    for row in sq:
        for item in row:
            r.append(item[0])
            g.append(item[1])
            b.append(item[2])
    r,g,b = np.array(r),np.array(g),np.array(b)
    for row in sq:
        for item in row