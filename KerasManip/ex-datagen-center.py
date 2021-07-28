# The three main types of pixel scaling techniques supported by the ImageDataGenerator class are as follows:
# - Pixel Normalization: scale pixel values to the range 0-1. 
# - Pixel Centering: scale pixel values to have a zero mean.
# - Pixel Standardization: scale pixel values to have a zero mean and unit variance.

# Centering a image dataset

from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print('-- Loaded dataset ----------------------------')
print('Train', train_images.shape, train_labels.shape)
print('Test', (test_images.shape, test_labels.shape))

print('Train Min=%.3f, Max=%.3f, Mean=%.5f, Std=%.5f' % (train_images.min(), train_images.max(), train_images.mean(), train_images.std()))
print('Test Min=%.3f, Max=%.3f, Mean=%.5f, Std=%.5f' % (test_images.min(), test_images.max(), test_images.mean(), test_images.std()))
print('---------------------------------------------')

# reshape dataset to have a single channel
width, height, channels = train_images.shape[1], train_images.shape[2], 1
train_images = train_images.reshape((train_images.shape[0], width, height, channels))
test_images = test_images.reshape((test_images.shape[0], width, height, channels))

print('Per image means')
print('Mean train=%.3f, test=%.3f' % (train_images.mean(), test_images.mean()))

# create data generator that centers pixel values
datagen = ImageDataGenerator(featurewise_center=True)

# calculate the mean of the training dataset
datagen.fit(train_images)
print('Data generator mean=%.3f' % datagen.mean)

# demonstrate effect on a single batch of samples
iterator = datagen.flow(train_images, train_labels, batch_size=64)

# get a batch
batchX, batchY = iterator.next()

print('Mean pixel value in the batch')
print('Shape %s, Mean=%.3f' % (batchX.shape, batchX.mean()))

# demonstrate effect on entire training dataset
iterator = datagen.flow(train_images, train_labels, batch_size=len(train_images), shuffle=False)

# get a batch
batchX, batchY = iterator.next()
print('Mean pixel value in the Entire Dataset')
print('Shape %s, Mean=%f' % (batchX.shape, batchX.mean()))

# zilvinas@zilvinas KerasManip % python ex-datagen-center.py
# -- Loaded dataset ----------------------------
# Train (60000, 28, 28) (60000,)
# Test ((10000, 28, 28), (10000,))
# Train Min=0.000, Max=255.000, Mean=33.31842, Std=78.56749
# Test Min=0.000, Max=255.000, Mean=33.79122, Std=79.17246
# ---------------------------------------------
# Per image means
# Mean train=33.318, test=33.791
# Data generator mean=33.318
# Mean pixel value in the batch
# Shape (64, 28, 28, 1), Mean=-0.485
# Mean pixel value in the Entire Dataset
# Shape (60000, 28, 28, 1), Mean=-0.000020
