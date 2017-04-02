# init libraries
import numpy as np
import tensorflow as tf


# this is to reveal codes of sigmoid neuron (sigmoid activation function)
# indepth view on this section is at .ipynb

def sigmoidFunction(z):
  return 1. / (1. + np.exp(-z))

z_sig = tf.nn.sigmoid(z)
