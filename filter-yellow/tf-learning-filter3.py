import glob
import cv2
import numpy as np
from PIL import Image

import tensorflow as tf
import itertools
import numpy as np
from numpy import genfromtxt
import base64




input_images = []
output_images = []
imgCount = 0
filterCount = 0




# Info during training run
tf.logging.set_verbosity(tf.logging.INFO)





# Input Function
def input_fn():



	input = []
	output = []

	for imgName in glob.glob('/Work/MyProjects/Python/filter-yellow/input-images/*.png'):

		image_contents = tf.read_file(imgName)
		image = tf.image.decode_image(image_contents, channels=3)
		input.append(image)

	print("----------------------")
	print("INPUT IMAGES LOADED")
	print("----------------------")

	for imgNameF in glob.glob('/Work/MyProjects/Python/filter-yellow/output-images/*.png'):

		image_contents = tf.read_file(imgNameF)
		image = tf.image.decode_image(image_contents, channels=3)
		output.append(image)

	print("----------------------")
	print("OUTPUT IMAGES LOADED")
	print("----------------------")


	# input = np.array(input)
	# output = np.array(output)


	return {"pixel": tf.convert_to_tensor(input)}, tf.convert_to_tensor(output)


print("INPUT_FN DONE")





# Estimator
features = [tf.contrib.layers.real_valued_column("pixel", dimension=3)]
print("FEATURES DONE")
estimator = tf.contrib.learn.DNNRegressor(feature_columns=features,
										  label_dimension=[50246, 3],
										  hidden_units=[259, 194],
										  model_dir="DNNRegressor259_194")
print("ESTIMATOR DONE")





# Train
estimator.fit(input_fn=input_fn)

print("TRAIN DONE")






# Evaluate
ev = estimator.evaluate(input_fn=input_fn, steps=1)
print("Loss: {0:f}" . format(ev["loss"]))







# Predictions
def predict_fn():

	images = []

	for i in range(470, 483):
		images.append(np.fromfile("bin/bin%06d.bin" % i, dtype='uint8'))

	images = np.array(images)

	return {"pixel": tf.convert_to_tensor(images)}

p = estimator.predict(input_fn=predict_fn)
predictions = list(itertools.islice(p, 6))
print("Predictions: {}".format(str(predictions)))






# if __name__ == "__main__":
# 	loadImages()
# 	createFilter()
# 	input_fn()
