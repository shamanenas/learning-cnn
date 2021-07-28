# The three main types of pixel scaling techniques supported by the ImageDataGenerator class are as follows:
# - Pixel Normalization: scale pixel values to the range 0-1. 
# - Pixel Centering: scale pixel values to have a zero mean.
# - Pixel Standardization: scale pixel values to have a zero mean and unit variance.

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

print('Train min=%.3f, max=%.3f' % (train_images.min(), train_images.max()))
print('Test min=%.3f, max=%.3f' % (test_images.min(), test_images.max()))

# create data generator
datagen = ImageDataGenerator(rescale=1.0/255.0)

train_iterator = datagen.flow(train_images, train_labels, batch_size=64)
test_iterator = datagen.flow(test_images, test_labels, batch_size=64)

print('Batches train=%d, test=%d' % (len(train_iterator), len(test_iterator)))

batchX, batchY = train_iterator.next()

print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))

# Running the example ﬁrst reports the minimum and maximum pixel value for the train and test datasets. 
# The MNIST dataset only has a single channel because the images are black and white (grayscale), 
# but if the images were color, the min and max pixel values would be calculated across all channels 
# in all images in the training dataset, i.e. there would not be a separate mean value for each channel.
# The ImageDataGenerator does not need to be ﬁt on the training dataset as there is nothing that needs to be calculated, 
# we have provided the scale factor directly. A single batch of normalized images is retrieved and 
# we can conﬁrm that the min and max pixel values are zero and one respectively.
#
# zilvinas@zilvinas KerasManip % python ex-datagen.py
# -- Loaded dataset ----------------------------
# Train (60000, 28, 28) (60000,)
# Test ((10000, 28, 28), (10000,))
# Train Min=0.000, Max=255.000, Mean=33.31842, Std=78.56749
# Test Min=0.000, Max=255.000, Mean=33.79122, Std=79.17246
# ---------------------------------------------
# Train min=0.000, max=255.000
# Test min=0.000, max=255.000
# Batches train=938, test=157
# Batch shape=(64, 28, 28, 1), min=0.000, max=1.000