import numpy as np
from PIL import Image
import json
import csv

f = open('inputset2/input.json' )
data = json.load(f)

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
