#
# Global Standardization
#
# The example below calculates the mean and 
# standard deviations across all color channels in the loaded image, 
# then uses these values to standardize the pixel values.

from PIL import Image
from numpy.core._asarray import asarray


image = Image.open('sydney_bridge.jpeg')
pixels = asarray(image)

print('Data Type: %s' % pixels.dtype)
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

# Convert integers to floats
pixels = pixels.astype('float32')

# Calculate global mean and standard deviation
mean, std = pixels.mean(), pixels.std()
print('Mean: %.3f, Standrd Deviation: %.3f' % (mean, std))

#global standardization of pixels
pixels = (pixels - mean) / std

mean, std = pixels.mean(), pixels.std()
print('After Global Standardization ==>')
print('Mean: %.3f, Standrd Deviation: %.3f' % (mean, std))


