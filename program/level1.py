import json
from PIL import Image,ImageGrab

f = open('input.json')

data = json.load(f)
img1=Image.open(r"wafer_image_1.png")
img1.show()
f.close()
