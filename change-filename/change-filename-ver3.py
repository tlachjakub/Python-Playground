import os

path = '/Users/jakubtlach/Desktop/Eyes_Data'
files = os.listdir(path)

for i, f in enumerate(files):
    src = os.path.join(path, f)
    dst = os.path.join(path, (str(i + 1)+'.png'))
    os.rename(src, dst)


print("IMAGES RENAMED")




