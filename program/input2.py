from PIL import Image
import json
import csv
import collections as cc
import numpy as np

def Exclusion(data):
    for exclusion in range(len(data['exclusion_zones'])):
        for y in range(data['exclusion_zones'][exclusion]['top_left']['x'], data['exclusion_zones'][exclusion]['bottom_right']['x']):
            for x in range(data['exclusion_zones'][exclusion]['bottom_right']['y'], data['exclusion_zones'][exclusion]['top_left']['y']):
                d_ex[tuple([y,x])] = 1

def inExclusion(i,j):
    if d_ex[tuple([i,j])] == 1:
        return True
    return False

f = open('inputset2/input.json' )
data = json.load(f)

d_ex = cc.defaultdict(int)
Exclusion(data)
l=[]
care_bottom=[]
care_top=[]
exclusion_bottom=[]
exclusion_top=[]
count=0
for ca in data['care_areas']:
    care_top.append(ca['top_left'])
    care_bottom.append(ca['bottom_right'])
for ca in data['care_areas']:
    exclusion_top.append(ca['top_left'])
    exclusion_bottom.append(ca['bottom_right'])
print(data['die']['columns'])
for k in range(1,data['die']['columns']*data['die']['rows']+1):

    image= Image.open('inputset2/wafer_image_10'+'.png')
    image_data = np.asarray(image)


    for a in range(len(care_bottom)):
        for i in range(care_bottom[a]['y'] , care_top[a]['y']):
            for j in range(care_top[a]['x']-1,care_bottom[a]['x']):
                next=image_data[i][j+1]
                current=image_data[i][j]
                prev = image_data[i][j-1]
                if (inExclusion(1,j) == False):
            #if((current[0]==prev[0] and current[1]==prev[1] and current[2]==prev[2]) or (current[0]==next[0] and current[1]==next[1] and current[2]==next[2])):
                     if((list(current)==list(prev)) or (list(current)==list(next))):
                        pass
                     else:
                        l.append([k,j,len(image_data)-i-1])


with open('output_2.csv', 'w+',newline="") as op:
    csv_writer = csv.writer(op)
    for i in l:
        csv_writer.writerow(i)