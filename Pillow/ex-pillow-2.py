from matplotlib import image
from matplotlib import pyplot

data = image.imread('Sydney-Opera-House.jpeg')

print(data.dtype)
print(data.shape)

pyplot.imshow(data)
pyplot.show()