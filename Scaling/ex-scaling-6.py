#
# Global Standardization SHIFTED to positive domain
#
# The example below calculates the mean and 
# standard deviations across all color channels in the loaded image, 
# then uses these values to standardize the pixel values.

from PIL import Image
from numpy.core._asarray import asarray
from numpy import clip


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

# Clip pixel values to [-1,1]
pixels = clip(pixels, -1.0, 1.0)

# Shift from [-1,1] to [0,1] with 0.5 mean
pixels = (pixels + 1.0) / 2.0

# Confirm it had the desired effect
mean, std = pixels.mean(), pixels.std()
print('After Global Standardization ==>')
print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))


