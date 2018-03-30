import PIL
from PIL import Image
import glob
import numpy as np

image_path = '/Work/MyProjects/Python/black-and-white/images/elon_musk.jpg'
image = Image.open(image_path)
pixdata = image.copy()
# pixdata = Image.new("RGB", (299, 299), "white")


#for filename in glob.glob("*.jpg"):
#   image = image.open(filename)
#    image = image.convert('1')
#    image.save()
#    print(filename)

#image = image.convert('1')
#image.save('result3.png')


#from PIL import Image

#image_path = '/path/to/image'
#image = Image.open(image_path)
#count = 0

# image.getdata() returns all the pixels in the image

x = 0
y = 0
for pixel in image.getdata():
    r, g, b = pixel
    r = 0
    pixel = r, g, b
    pixdata.putpixel((x, y), pixel)
    print(pixel)

    x = x + 1
    if x >= 299:
        x = 0
        y = y + 1


pixdata.save("/Work/MyProjects/Python/black-and-white/images/elon_muskZZZZ2.jpg")



