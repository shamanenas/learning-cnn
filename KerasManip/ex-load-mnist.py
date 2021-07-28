# load mnist database
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print('Train', train_images.shape, train_labels.shape)
print('Test', (test_images.shape, test_labels.shape))

print('Train', train_images.min(), train_images.max(), train_images.mean(), train_images.std())
print('Test', test_images.min(), test_images.max(), test_images.mean(), test_images.std())

# zilvinas@zilvinas KerasManip % python ex-load-mnist.py
# Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
# 11493376/11490434 [==============================] - 1s 0us/step
# 11501568/11490434 [==============================] - 1s 0us/step
# Train (60000, 28, 28) (60000,)
# Test ((10000, 28, 28), (10000,))
# Train 0 255 33.318421449829934 78.56748998339798
# Test 0 255 33.791224489795916 79.17246322228644
