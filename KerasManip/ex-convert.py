# Loading image with Keras API

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array, array_to_img

img = load_img('bondi_beach.jpg')

print(type(img))
img_array = img_to_array(img)

print(img_array.dtype)

img_pil = array_to_img(img_array)
print(type(img_pil))

img_pil.show()
