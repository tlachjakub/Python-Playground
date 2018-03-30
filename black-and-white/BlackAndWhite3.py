import PIL
from PIL import Image
import glob
import numpy as np
import sys

image_path = '/Work/MyProjects/Python/black-and-white/images/elon_musk.jpg'
img = Image.open(image_path)
img = img.convert("RGBA")

pixdata = img.load()

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x,y] == (255, 255, 255, 255):
            print(pixdata)
            pixdata[x,y] = (0, 0, 0, 255)
            print(pixdata)

img = pixdata

print(pixdata)





