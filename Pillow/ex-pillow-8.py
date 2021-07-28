#
# Resize Image
# resize & IGNORE aspect ratio
#

from PIL import Image

image = Image.open('Sydney-Opera-House.jpeg')
print("Size:   ", image.size)

# resize & fore aspect ratio
# default is a bicubic resampling algorithm
img_resized = image.resize((200,200))

print("T Size: ", img_resized.size)

img_resized.show()

