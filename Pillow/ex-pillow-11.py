#
# CROPP
#

from PIL import Image
from matplotlib import pyplot

image = Image.open('Sydney-Opera-House.jpeg')
print("Size:   ", image.size)

cropped = image.crop((100, 100, 200, 200))

cropped.show()
