import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(10).astype(np.float32)
y_data = x_data * 0.1 + 0.3

print(x_data)
print(y_data)

### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
sqr = tf.square(y - y_data)
loss = tf.reduce_mean(sqr)
# initial optimizer with a approach method and approach speed(learning rate)
optimizer = tf.train.GradientDescentOptimizer(0.5)
# use this optimizer to get the minima of loss funciton
train = optimizer.minimize(loss) 

init = tf.global_variables_initializer()
### create tensorflow structure end ###

# ensorFlow does not actually run any computation 
# until the session is created and the run function is called.
sess = tf.Session()
sess.run(init)

for step in range(21):
    sess.run(train)
    print(step, sess.run(sqr), sess.run(Weights), sess.run(biases))



