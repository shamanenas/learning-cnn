# Example multilayer perceptron
# We deﬁned a Multilayer Perceptron model for binary classiﬁcation. 
# The model has:
#  - 10 inputs, 
#  - 3 hidden layers with 10, 20, and 10 neurons, and 
#  - an output layer with 1 output.
#  
#  Rectiﬁed linear activation functions (ReLU) are used in each hidden layer and 
#  a sigmoid activation function is used in the output layer, 
#  for binary classiﬁcation.

from keras import models
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input, Dense
from numpy.core.numeric import outer

#Construct model
visible = Input(shape=(10,))
hidden1 = Dense(10, activation='relu')(visible)
# The dense layer is a neural network layer that is connected deeply, 
# which means each neuron in the dense layer receives input from _all_ neurons of its previous layer
#
# Dense implements the operation: 
# output = activation(dot(input, kernel) + bias) 
# where
#   activation is the element-wise activation function passed as the activation argument, 
#   kernel is a weights matrix created by the layer, and 
#   bias is a bias vector created by the layer (only applicable if use_bias is True). 
# dot funkcija - dvieju vektoriu skaliarine sandauga a•b = a b cos 𝜽

hidden2 = Dense(20, activation='relu')(hidden1)
hidden3 = Dense(10, activation='relu')(hidden2)
output = Dense(1, activation='sigmoid')(hidden3)
model = Model(inputs=visible, outputs=output)

# sumarize layers
model.summary()

# plot graph
plot_model(model, to_file='ex-mlp.png')

# _________________________________________________________________
# Layer (type)                 Output Shape              Param #
# =================================================================
# input_1 (InputLayer)         [(None, 10)]              0
# _________________________________________________________________
# dense (Dense)                (None, 10)                110
# _________________________________________________________________
# dense_1 (Dense)              (None, 20)                220
# _________________________________________________________________
# dense_2 (Dense)              (None, 10)                210
# _________________________________________________________________
# dense_3 (Dense)              (None, 1)                 11
# =================================================================
# Total params: 551
# Trainable params: 551
# Non-trainable params: 0