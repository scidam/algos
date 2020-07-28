import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# all experiments should be reproducible
np.random.seed(10)

# Generate random values 
X = np.random.rand(100, 10)
Y = np.random.rand(100)

W = tf.Variable(np.random.randn(10, 1))
b = tf.Variable(np.random.randn(100))


def loss_function(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

def linreg_model(x):
    return X @ W + b

loss_values = list()

def train_model(niter=1000, learning_rate=1.0e-1):
    global W, b
    for k in range(niter):
        print(f"Current step is {k}")
        with tf.GradientTape() as g:
            y_pred = linreg_model(X)
            loss = loss_function(Y, y_pred)
        gradient = g.gradient(loss, [W, b])
        W.assign(W.numpy() - gradient[0] * learning_rate)
        b.assign(b.numpy() - gradient[1] * learning_rate)
        print(f"Loss' function value is {loss}.")
        loss_values.append(loss.numpy())


train_model()

plt.plot(loss_values)
plt.savefig('output.png')