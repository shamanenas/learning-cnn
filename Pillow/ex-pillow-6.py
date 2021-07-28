#
# convert to grayscale and save images
#

from PIL import Image

image = Image.open('Sydney-Opera-House.jpeg')
print(image.format)

gs_image = image.convert(mode='L')

gs_image.save('opera-gs.jpeg')

image2 = Image.open('opera-gs.jpeg')
print(image2.format)

image2.show()

