import numpy as np
import tensorflow as tf

x = tf.placeholder(tf.float32)  # may pass n-dimension list
beta = tf.Variable([1.])  # tf.float32 is implicitly defined; keep dimensions relevant
alpha = tf.Variable([5.])

y_true = tf.placeholder()
y = tf.matmul(x, beta) + alpha  # basic linear model
# matmul is matrix multiplication

cross_entropy = tf.reduce_mean(
  tf.nn.sigmoid_cross_entropy_with_logits(labels=y_true, logits=y)
)  # labels equals to target, y serves as preds
# This formulae is needed to escape calculation issues


# session run
ses = tf.Session()
init = tf.global_variables_initializer()
ses.run(init)
print(sess.run(y, {x: [1, 2, 3, 4]}))

print(sess.run(cross_entropy, {x: [1, 2, 3, 4], y_true: [-5.5, -6.5, 7.5, 8.5]}))


# manual sigmoid function and cross-entropy loss

def sigmoidFunction(pred):
  return 1 / (np.exp(-pred))

def crossEntropy(y_true, pred=y):
  return np.mean(-np.sum(y_true * np.log(sigmoidFunction(pred))))
