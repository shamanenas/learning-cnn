#
# Resize Image
# resize & preserve aspect ratio
#

from PIL import Image

image = Image.open('Sydney-Opera-House.jpeg')
print("Size:   ", image.size)

# resize & preserve aspect ratio
image.thumbnail((100,100))

print("T Size: ", image.size)

image.show()

