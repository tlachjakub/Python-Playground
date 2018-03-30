import os
import glob


def listdir_nohidden(path):
	return glob.glob(os.path.join(path, '*'))



path = 'test'
files = listdir_nohidden(path)
count = 0


for file in files:
	os.rename(file, os.path.join(path, str(count)+'.png'))
	count = count + 1
	print('DONE')


print("IMAGES RENAMED")




