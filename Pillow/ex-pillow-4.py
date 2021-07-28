#
# # load images from folder
#

from os import listdir
from matplotlib import image, pyplot

loaded_images = list()

for filename in listdir('images'):
    img_data = image.imread('images/' + filename)

    loaded_images.append(img_data)
    print('> loaded %s %s' % (filename, img_data.shape))

for image in loaded_images:
    pyplot.imshow(image)
    pyplot.show()
