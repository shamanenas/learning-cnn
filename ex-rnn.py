# example of a recurrent neural network 

# a long short-term memory recurrent neural network for sequence classiﬁcation. 
#  The model expects 100 time steps of one feature as input. 
#  The model has a single LSTM hidden layer to extract features from the sequence, 
#   followed by a fully connected layer to interpret the LSTM output, 
#   followed by an output layer for making binary predictions

from keras import models
from keras.utils import vis_utils
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input, Dense
from keras.layers.recurrent import LSTM

visible = Input(shape=(100,1))
hidden1 = LSTM(10)(visible)
hidden2 = Dense(10, activation='relu')(hidden1)
output = Dense(1, activation='sigmoid')(hidden2)

model = Model(inputs=visible, outputs=output)

model.summary()

plot_model(model, to_file='ex_rnn.png')