#
# Normalization
#
from PIL import Image
from numpy.core._asarray import asarray


image = Image.open('sydney_bridge.jpeg')
pixels = asarray(image)

print('Data Type: %s' % pixels.dtype)
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))


pixels = pixels.astype('float32')
print('Data Type: %s' % pixels.dtype)
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

pixels /= 255.0
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))


# image2 = Image.fromarray(pixels)
# image2.show()

