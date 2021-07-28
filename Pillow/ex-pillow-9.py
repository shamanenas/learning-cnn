#
# FLIP
#

from PIL import Image
from matplotlib import pyplot

image = Image.open('Sydney-Opera-House.jpeg')
print("Size:   ", image.size)

# H Flip
h_flip = image.transpose(Image.FLIP_LEFT_RIGHT)

# V Flip
v_flop = image.transpose(Image.FLIP_TOP_BOTTOM)

pyplot.subplot(311)
pyplot.imshow(image)

pyplot.subplot(312)
pyplot.imshow(h_flip)

pyplot.subplot(313)
pyplot.imshow(v_flop)

pyplot.show()
