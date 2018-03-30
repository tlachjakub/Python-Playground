import os

path = '/Users/jakubtlach/Desktop/Eyes_Data/okubutae/'
files = os.listdir(path)
count = 0


for file in files:

    os.rename(os.path.join(path, file), os.path.join(path, str(count)+'.png'))
    count = count + 1
    print('DONE')


print("IMAGES RENAMED")




