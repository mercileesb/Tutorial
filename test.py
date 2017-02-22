import tensorflow as tf

hello = tf.constant("12")
sess = tf.Session()

print sess.run(hello)