import json
from PIL import Image
import numpy
import collections as cc

f = open('input.json' )
data = json.load(f)

for i in range(1,data['die']['columns']+1):
    im = Image.open('wafer_image_'+str(i)+'.png')
    px = im.load()
    width,height = im.size
    numpydata = numpy.array(im)
    ans = []
    for x in range(len(numpydata)):
        d = cc.defaultdict(int)
        for y in range(len(numpydata[i])):
            d[numpydata[x][y][0]] += 1
        m = 0
        for z in d:
            if(d[z] > m):
                temp = x
                m = d[z]
        for y in range(len(numpydata[i])):
            if(numpydata[i][y][0] != temp):
                ans.append([i,x,y])
    print(ans)


f.close()
