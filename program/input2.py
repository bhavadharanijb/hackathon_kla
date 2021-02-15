from PIL import Image
import json
import csv
import numpy as np

f = open('inputset2/input.json' )
data = json.load(f)
#print(data)
l=[]
care_bottom=[]
care_top=[]
exclusion_bottom=[]
exclusion_top=[]

for ca in data['care_areas']:
    care_top.append(ca['top_left'])
    care_bottom.append(ca['bottom_right'])
for ca in data['care_areas']:
    exclusion_top.append(ca['top_left'])
    exclusion_bottom.append(ca['bottom_right'])

for k in range(1,data['die']['columns']+1):


    image= Image.open('inputset2/wafer_image_'+str(k)+'.png')
    image_data = np.asarray(image)


    for i in range(len(image_data)):
        for j in range(1,len(image_data[0])-1):
            next=image_data[i][j+1]
            current=image_data[i][j]
            prev = image_data[i][j-1]
            #if((current[0]==prev[0] and current[1]==prev[1] and current[2]==prev[2]) or (current[0]==next[0] and current[1]==next[1] and current[2]==next[2])):
            if((list(current)==list(prev)) or (list(current)==list(next))):
                pass
            else:
                l.append([k,j,len(image_data)-i-1])
final=[]
for j in range(len(care_bottom)):
    for i in l:
        if(i[1]>=care_top[j]['x'] and i[1]<=care_bottom[j]['x'] and i[2]<=care_top[j]['y'] and i[2]>=care_bottom[j]['y']):
            if(i[1]<exclusion_top[j]['x'] and i[1]>exclusion_bottom[j]['x'] and i[2]>exclusion_top[j]['y'] and i[2]<exclusion_bottom[j]['y']):
                final.append(l)
print(final)
with open('output_2.csv', 'w+') as op:
    csv_writer = csv.writer(op)
    for i in l:
        csv_writer.writerow(i)