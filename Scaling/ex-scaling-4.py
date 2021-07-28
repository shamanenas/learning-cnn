#
# Local Centering
#
# Global Centering: Calculating and subtracting the mean pixel value across color channels.
# Local Centering: Calculating and subtracting the mean pixel value per color channel.

from PIL import Image
from numpy.core._asarray import asarray


image = Image.open('sydney_bridge.jpeg')
pixels = asarray(image)

print('Data Type: %s' % pixels.dtype)
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

# Convert integers to floats
pixels = pixels.astype('float32')

# Calculate per-channel means and standard deviations
means = pixels.mean(axis=(0,1), dtype='float64')

print('Means %s' % means)
print('Mins: %s, Maxs: %s' % (pixels.min(axis=(0,1)), pixels.max(axis=(0,1))))

pixels -= means

means = pixels.mean(axis=(0,1), dtype='float64')

print('Means %s' % means)
print('Mins: %s, Maxs: %s' % (pixels.min(axis=(0,1)), pixels.max(axis=(0,1))))


# image2 = Image.fromarray(pixels)
# image2.show()

