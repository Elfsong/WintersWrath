import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer

    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.truncated_normal([in_size, out_size], stddev=0.1), name="W")
            tf.summary.histogram(layer_name + '/weights', Weights)

        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name="b")
            tf.summary.histogram(layer_name + '/biases', biases)

        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases

        outputs = tf.nn.dropout(Wx_plus_b, 0.75)

        if activation_function:
            outputs = activation_function(Wx_plus_b)

        tf.summary.histogram(layer_name + '/outputs', outputs)

        return outputs


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 784])  # 28x28
    ys = tf.placeholder(tf.float32, [None, 10])

layer_1 = add_layer(xs, 784, 60, n_layer=1, activation_function=tf.nn.relu)
prediction = add_layer(layer_1, 60, 10, n_layer=2, activation_function=tf.nn.softmax)

# Loss
with tf.name_scope('loss'):
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
    tf.summary.scalar('loss', cross_entropy)

# Train
with tf.name_scope('Train'):
    train_step = tf.train.GradientDescentOptimizer(0.4).minimize(cross_entropy)

# Establish Session
sess = tf.Session()

merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("logs/", sess.graph)
init = tf.global_variables_initializer()

sess.run(init)
sess.run(tf.global_variables_initializer())

for i in range(3000):
    # training
    batch_xs, batch_ys = mnist.train.next_batch(600)
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})

    if i % 50 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))
