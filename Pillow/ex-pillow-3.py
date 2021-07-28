#
# # Converting image to NumPy Array and Back
#

from PIL import Image
from numpy.core._asarray import asarray

image = Image.open('Sydney-Opera-House.jpeg')

data = asarray(image)

print(type(data))
print("Array shape: {}".format(data.shape))

image2 = Image.fromarray(data)

print("Format: ", image2.format)
print("Mode:   ", image2.mode)
print("Size:   ", image2.size)

image2.show()