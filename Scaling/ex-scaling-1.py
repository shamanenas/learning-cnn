from PIL import Image

image = Image.open('sydney-bridge.png')

print(image.format)
print(image.mode)
print(image.size)

image.show()