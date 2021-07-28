#
# Local Standardization 
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

# Calculate per channel mean and standard deviation
means = pixels.mean(axis=(0,1), dtype='float64')
stds = pixels.std(axis=(0,1), dtype='float64')

print('Means: %s, Standard Deviations: %s' % (means, stds))

# Per channel standardization of pixels
pixels = (pixels - means) / stds

# Confirm it had the desired effect
means, stds = pixels.mean(axis=(0,1), dtype='float64'), pixels.std(axis=(0,1), dtype='float64')
print('After Local Standardization ==>')
print('Means: %s' % means) 
print('Standard Deviations: %s' % (stds))


