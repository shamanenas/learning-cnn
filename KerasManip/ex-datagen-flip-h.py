# Image augmentation with ImageDataGenerator

# Steps
# 1. Prepare images dataset
# 2. create ImageDataGenerator
# 3. Create iterators flow() or flow_from_directory(...)
# 4. Fit 

# Horizontal shift image augmentation

from PIL import Image
from numpy import expand_dims
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from matplotlib import pyplot
img = load_img('bird.jpg')

data = img_to_array(img)

# expand dimension to one sample
samples = expand_dims(data, 0)

dgen = ImageDataGenerator(horizontal_flip=True)

# make iterator
it = dgen.flow(samples, batch_size=1)

# gen samples and plot
for i in range(9):
    pyplot.subplot(330 + 1 + i)
    # Generate batch of images
    batch = it.next()
    # convert to unsigned ints for viewing
    image = batch[0].astype('uint8')
    pyplot.imshow(image)
pyplot.show()