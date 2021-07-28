from PIL import Image

img = Image.open('Sydney-Opera-House.jpeg')

print(img.format)
print(img.mode)
print(img.size)
img.show()