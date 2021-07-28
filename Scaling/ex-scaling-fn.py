#
# Local Standardization 
#
# The example below calculates the mean and 
# standard deviations across all color channels in the loaded image, 
# then uses these values to standardize the pixel values.

from PIL import Image
from numpy.core._asarray import asarray
from numpy import clip

def normalize(pixels):
    pixels /= 255.0
    return pixels

def global_centering(pixels):
    mean = pixels.mean()
    pixels = pixels - mean
    return pixels

def local_centering(pixels):
    # Calculate per-channel means and standard deviations
    means = pixels.mean(axis=(0,1), dtype='float64')
    pixels -= means
    return pixels

def global_standardization(pixels): 
    # Calculate global mean and standard deviation
    mean, std = pixels.mean(), pixels.std()
    pixels = (pixels - mean) / std
    return pixels

def global_standardization_shifted(pixels):
    pixels = global_standardization(pixels)

    # Clip pixel values to [-1,1]
    pixels = clip(pixels, -1.0, 1.0)

    # Shift from [-1,1] to [0,1] with 0.5 mean
    pixels = (pixels + 1.0) / 2.0
    return pixels

def local_standardization(pixels):
    # Calculate per channel mean mean and standard deviation
    means = pixels.mean(axis=(0,1), dtype='float64')
    stds = pixels.std(axis=(0,1), dtype='float64')
    pixels = (pixels - means) / stds
    return pixels
    
def scale_image(img_path, transformation):
    switch = {
        'normalize': normalize,
        'global_centering': global_centering,
        'local_centering': local_centering,
        'global_standardization': global_standardization,
        'global_standardization_shifted': global_standardization_shifted, 
        'local_standardization': local_standardization
    }

    image = Image.open(img_path)
    pixels = asarray(image)
    print('** Input *******************************')
    print('*  Data Type: %s' % pixels.dtype)
    print('*  Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))
    print('*  Mean: %.3f' % pixels.mean())

    # Convert integers to floats
    pixels = pixels.astype('float32')

    f = switch.get(transformation, "nothing")
    return f(pixels)

img_path = 'sydney_bridge.jpeg'

print("Normalized:")
pixels = scale_image(img_path, 'normalize')
print('** OUTPUT')
print('*  Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))
print('* ------------------------------------------')

print("Global centered:")
pixels = scale_image(img_path, 'global_centering')
mean = pixels.mean()
print('** OUTPUT')
print('Mean %.3f' % mean)
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))
print('------------------------------------------')

print("Local centered:")
pixels = scale_image(img_path, 'local_centering')
means = pixels.mean(axis=(0,1), dtype='float64')
print('** OUTPUT')
print('Means %s' % means)
print('Mins: %s, Maxs: %s' % (pixels.min(axis=(0,1)), pixels.max(axis=(0,1))))
print('------------------------------------------')

print("Global STD:")
pixels = scale_image(img_path, 'global_standardization')
mean, std = pixels.mean(), pixels.std()
print('** OUTPUT')
print('Mean: %.3f, Standrd Deviation: %.3f' % (mean, std))
print('------------------------------------------')

print("Global STD SHIFTED:")
pixels = scale_image(img_path, 'global_standardization_shifted')
mean, std = pixels.mean(), pixels.std()
print('** OUTPUT')
print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))
print('------------------------------------------')

print("Local STD :")
pixels = scale_image(img_path, 'local_standardization')
means, stds = pixels.mean(axis=(0,1), dtype='float64'), pixels.std(axis=(0,1), dtype='float64')
print('** OUTPUT')
print('Means: %s' % means) 
print('Standard Deviations: %s' % (stds))
print('------------------------------------------')