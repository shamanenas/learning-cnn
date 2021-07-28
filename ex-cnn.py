# Example CNN

# The model receives black and white 64 × 64 images as input, 
#   then has a sequence of two convolutional  and 
#     pooling layers as feature extractors, 
#       followed by a fully connected layer to interpret the features and 
#         an output layer with a sigmoid activation for two-class predictions

from keras import models
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input, Dense, Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D

# layers
visible = Input(shape=(64, 64, 1))
conv1 = Conv2D(32, (4,4), activation='relu')(visible)
pool1 = MaxPooling2D()(conv1)
conv2 = Conv2D(16, (4,4), activation='relu')(pool1)
pool2 = MaxPooling2D()(conv2)
flat1 = Flatten()(pool2)
hidden1 = Dense(10, activation='relu')(flat1)
output = Dense(1, activation='sigmoid')(hidden1)

# model
model = Model(inputs=visible, outputs=output)

# sumarize
model.summary()

#plot model
plot_model(model, to_file='ex-cnn.png')

# _________________________________________________________________
# Layer (type)                 Output Shape              Param #
# =================================================================
# input_1 (InputLayer)         [(None, 64, 64, 1)]       0
# _________________________________________________________________
# conv2d (Conv2D)              (None, 61, 61, 32)        544
# _________________________________________________________________
# max_pooling2d (MaxPooling2D) (None, 30, 30, 32)        0
# _________________________________________________________________
# conv2d_1 (Conv2D)            (None, 27, 27, 16)        8208
# _________________________________________________________________
# max_pooling2d_1 (MaxPooling2 (None, 13, 13, 16)        0
# _________________________________________________________________
# flatten (Flatten)            (None, 2704)              0
# _________________________________________________________________
# dense (Dense)                (None, 10)                27050
# _________________________________________________________________
# dense_1 (Dense)              (None, 1)                 11
# =================================================================
# Total params: 35,813
# Trainable params: 35,813
# Non-trainable params: 0
# _________________________________________________________________