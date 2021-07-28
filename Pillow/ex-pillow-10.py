#
# ROTATE
#

from PIL import Image
from matplotlib import pyplot

image = Image.open('Sydney-Opera-House.jpeg')
print("Size:   ", image.size)

pyplot.subplot(311)
pyplot.imshow(image)

pyplot.subplot(312)
pyplot.imshow(image.rotate(45))

pyplot.subplot(313)
pyplot.imshow(image.rotate(90))

pyplot.show()
