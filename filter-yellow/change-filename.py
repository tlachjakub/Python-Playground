import PIL
from PIL import Image
import glob
import numpy as np
import cv2
import os

img_array = []
count = 0

for img in glob.glob('/Work/MyProjects/Python/filter-yellow/input-images/*.jpg'):

    os.rename(img, str(count) + '.png')

    print('DONE')
    count += 1

print("IMAGES RENAMED")




