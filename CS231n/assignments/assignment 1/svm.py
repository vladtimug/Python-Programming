import random
import numpy as np
from cs231n.data_utils import load_CIFAR10
import matplotlib.pyplot as plt
from cs231n.classifiers.linear_svm import svm_loss_naive
import time
from cs231n.gradient_check import grad_check_sparse
from cs231n.classifiers.linear_svm import svm_loss_vectorized
# from __future__ import print_function

# CIFAR-10 Data loading and processing
# Load the raw CIFAR-10 data
cifar10_dir = "cs231n/datasets/cifar-10-batches-py"
X_train, y_train, X_test, y_test = load_CIFAR10(cifar10_dir)

# As a sanity check print the shapes of all the training and test data
# print("Training data shape:", X_train.shape)
# print("Training labels data shape:", y_train.shape)
# print("Testing data shape:", X_test.shape)
# print("Testing labels data shape:", y_test.shape)

# Visualize some examples of each class from the dataset
classes = [
    'plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship',
    'truck'
]
# num_classes = len(classes)
# samples_per_class = 7
# for y, clss in enumerate(classes):
#     # print("pos:", y, 'class:', clss)
#     idxs = np.flatnonzero(y_train == y)
#     idxs = np.random.choice(idxs, samples_per_class, replace=False)
#     for i, idx in enumerate(idxs):
#         plt_idx = i * num_classes + y + 1
#         plt.subplot(samples_per_class, num_classes, plt_idx)
#         plt.imshow(X_train[idx].astype('uint8'))
#         plt.axis('off')
#         if i == 0:
#             plt.title(clss)
# plt.show()

# Split the data into train, val and test sets. In addition we will
# create a small development set as a subset of the training data;
# we can use this for development so the code runs faster
num_training = 49000
num_validation = 1000
num_test = 1000
num_dev = 500

# The validation set will be num_validation points from the original training set
mask = range(num_training, num_training + num_validation)
X_val = X_train[mask]
y_val = y_train[mask]

# The training set will be the first num_training points from the original training set
mask = range(num_training)
X_train = X_train[mask]
y_train = y_train[mask]

# The development set, whish is a small subset of the training set
mask = np.random.choice(num_training, num_dev, replace=False)
X_dev = X_train[mask]
y_dev = y_train[mask]

# Use the first num_test points of the original test set as our test set
mask = range(num_test)
X_test = X_test[mask]
y_test = y_test[mask]

# print("Train data shape:", X_train.shape)
# print("Train labels shape:", y_train.shape)
# print("Validation data shape:", X_val.shape)
# print("Validation labels shape:", y_val.shape)
# print("Test data shape:", X_test.shape)
# print("Test labels shape:", y_test.shape)

# Preprocessing: reshape the image data into rows
X_train = X_train.reshape(X_train.shape[0], -1)
X_val = X_val.reshape(X_val.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)
X_dev = X_dev.reshape(X_dev.shape[0], -1)

# Print the current shape of all data sets as a sanity check
print("Train data shape:", X_train.shape)
print("Validation data shape:", X_val.shape)
print("Test data shape:", X_test.shape)

# Preprocessing: subtract the mean image
# First: compute the image mean based on the training image data
mean_image = np.mean(X_train, axis=0)
# print(mean_image[:10])  # print a few of the elements
# plt.figure(figsize=(4, 4))
# plt.imshow(mean_image.reshape(
#     (32, 32, 3)).astype('uint8'))  # visualize the mean image
# plt.show()

# Second: subtract the mean image from the train and test data to scale it down
X_train -= mean_image
X_val -= mean_image
X_test -= mean_image
X_dev -= mean_image

# Third: append the bias dimension of ones (i.e. bias trick) so that the SVM
# only has to worry about optimizing a single weight matrix W.
X_train = np.hstack([X_train, np.ones((X_train.shape[0], 1))])
X_val = np.hstack([X_val, np.ones((X_val.shape[0], 1))])
X_test = np.hstack([X_test, np.ones((X_test.shape[0], 1))])
X_dev = np.hstack([X_dev, np.ones((X_dev.shape[0], 1))])

print("\nImages")
print(
    "Training set shape: {}\nValidate set shape: {}\nTest set shape: {}\nDevelopment set shape: {}\nOne element of image set has shape: {}"
    .format(X_train.shape, X_val.shape, X_test.shape, X_dev.shape,
            X_dev[0].shape))
print("\nLabels")
print(
    "Training set shape: {}\nValidate set shape: {}\nTest set shape: {}\nDevelopment set shape: {}"
    .format(y_train.shape, y_val.shape, y_test.shape, y_dev.shape))

# Generate a random svm weight matrix of small numbers
W = np.random.randn(3073, 10) * 0.0001

# Numerically compute the gradient along several randmoly chosen dimensions, and
# compare them with the analytically computed gradient.
# f = lambda w: svm_loss_naive(w, X_dev, y_dev, 0.0)[0]
# grad_numerical = grad_check_sparse(f,W, grad)

# Do the gradient check again with regularization turned on
loss_naive, grad = svm_loss_naive(W, X_dev, y_dev, 5e1)
f = lambda w: svm_loss_naive(w, X_dev, y_dev, 5e1)[0]
grad_numerical = grad_check_sparse(f, W, grad)

tic = time.time()
loss_vectorized, _ = svm_loss_vectorized(W, X_dev, y_dev, 0.000005)
toc = time.time()
print("Vectorized loss: %e computed in %fs" % (loss_vectorized, toc-tic))
print("Difference: %f" % (loss_naive - loss_vectorized))