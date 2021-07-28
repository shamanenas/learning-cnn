# Convert to grayscale and save

from keras.preprocessing.image import load_img, save_img
from keras.preprocessing.image import img_to_array

file_name = 'bondi_beach'
file_ext = '.jpg'
file = file_name + file_ext
file_g = file_name + '_g' + file_ext

img = load_img(file, color_mode='grayscale')

print(type(img))

img_array = img_to_array(img)

save_img(file_g, img_array)

img = load_img(file_g)

print(type(img))
print(img.format)
print(img.mode)
print(img.size)
img.show()

