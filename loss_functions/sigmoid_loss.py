import numpy as np
import tensorflow as tf

x = tf.placeholder(tf.float32, [10.])  # may pass n-dimension list
beta = tf.placeholder([0])  # tf.float32 is implicitly defined; keep dimensions relevant
alpha = tf.placeholder([0])

y = tf.matmul(x, beta) + alpha  # basic linear model
# matmul is matrix multiplication

cross_entropy = tf.reduce_mean(
  tf.nn.sigmoid_cross_entropy_with_logits(labels=y_true, logits=y)
)  # labels equals to target, y serves as preds

#
#
# Manual sigmoid function and cross-entropy loss

def sigmoidFunction(pred):
  return 1 / (np.exp(-pred))

def crossEntropy(y_true, pred=y):
  return np.mean(-np.sum(y_true * np.log(sigmoidFunction(pred))))
