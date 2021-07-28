# Loading image with Keras API

from keras.preprocessing.image import load_img

img = load_img('bondi_beach.jpg')

print(type(img))
print(img.format)
print(img.mode)
print(img.size)

img.show()