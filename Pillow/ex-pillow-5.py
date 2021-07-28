#
# save images
#

from PIL import Image

image = Image.open('Sydney-Opera-House.jpeg')
print(image.format)

image.save('opera.png', format='PNG')

image2 = Image.open('opera.png')
print(image2.format)

image2.show()

