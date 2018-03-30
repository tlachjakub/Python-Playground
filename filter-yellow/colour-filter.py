import PIL
from PIL import Image
import glob
import numpy as np
import cv2
import os

img_array = []
count = 0

for img in glob.glob('/Work/MyProjects/Python/filter-yellow/output-images/*.png'):

    # TO DO - make same name like the original image by the saving with filter
    temp = cv2.imread(img)

    r, g, b = np.array(temp).T

    a = np.zeros_like(g)
    a[g < 100] = 255

    g = np.zeros_like(g)
    g[g < 100] = 0

    b = np.zeros_like(b)
    b[b < 100] = 0

    r = np.zeros_like(r)
    r[r < 100] = 255

    g = (b + r) * 60

    temp = Image.fromarray(np.dstack([item.T for item in (r, g, b, a)]))
    img_array.append(temp)
    temp.save("example%s.png" % count)

    print('DONE')
    count += 1

print('FINISHED')




