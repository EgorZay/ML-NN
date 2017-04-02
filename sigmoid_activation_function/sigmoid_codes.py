# init libraries
import numpy as np
import tensorflow as tf

# define weights, biases, inputs and outputs
w = tf.Variable([0.], tf.float32)
b = tf.Variable([0.], tf.float32)
x = tf.placeholder(tf.float32)
z = tf.matmul(w, x) + b

# evaluate sigmoid functions to pass to neurons
z_sigmoid = tf.nn.sigmoid(z)
# sigmoid = tf.nn.sigmoid(tf.matmul(w, x) + b)

def sigmoidFunction(z):
    return 1 / (1 + np.exp(-z))
