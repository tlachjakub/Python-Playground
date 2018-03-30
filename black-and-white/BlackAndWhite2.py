import PIL
from PIL import Image
import glob
import numpy as np
import cv2
import os


image_path = '/Work/MyProjects/Python/black-and-white/images/style1.jpg'
image = Image.open(image_path)

r, g, b = np.array(image).T

a = np.zeros_like(g)
a[g < 100] = 255

g = np.zeros_like(g)
g[g < 100] = 190

b = np.zeros_like(b)
b[b < 100] = 0

r = np.zeros_like(r)
r[r < 100] = 255

g = (b + r) * 50


image = Image.fromarray(np.dstack([item.T for item in (r,g,b,a)]))
image.save('style2.png')






