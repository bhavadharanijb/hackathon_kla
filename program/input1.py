import numpy as np
from PIL import Image
import json
import csv

f = open('input.json' )
data = json.load(f)

for k in range(1,data['die']['columns']+1):
    image= Image.open('wafer_image_'+str(k)+'.png')
    image_data = np.asarray(image)

    print(len(image_data[0]))
    l=[]
    with open('output.csv','w') as op:
        csv_writer=csv.writer(op)
        for i in range(len(image_data)):
            for j in range(1,len(image_data[0])-1):
                current=image_data[i][j]
                prev=image_data[i][j-1]
                next=image_data[i][j+1]
                if ((current[0]==prev[0] and current[1]==prev[1] and current[2]==prev[2] ) or (current[0]==next[0] and current[1]==next[1] and current[2]==next[2])):
                    pass
                else:
                    l.append([k,i,j])
        for i in l:
            csv_writer.writerow((i))
    #csv_writer.close()