# from __future__ import print_function
import random
import numpy as np
import matplotlib.pyplot as plt
from cs231n.data_utils import load_CIFAR10
from cs231n.classifiers import KNearestNeighbor

# plt.rcParams['figure.figsize'] = (
#     10.0, 8.0)  # set default size of plots using runtimeConfigurartions
# plt.rcParams['image.interpolation'] = 'nearest'
# plt.rcParams['image.cmap'] = 'gray'

cifar10_dir = 'cs231n/datasets/cifar-10-batches-py'

X_train, y_train, X_test, y_test = load_CIFAR10(cifar10_dir)
X_train_raw, y_train_raw, X_test_raw, y_test_raw = X_train, y_train, X_test, y_test
#Data set mapping
# X_train == 50.000 images
# y_train == 50.000 labels	#The number at index i indicates the label of the ith image in the array data
# X_test == 10.000 images
# y_test == 10.000 labels

print('Training, data shape - X_train: ',
      X_train.shape)  # images for training alg
print('Training labels shape - y_train: ',
      y_train.shape)  # labels for each image in the dataset
print('Test data shape - X_test.shape:', X_test.shape)  # images for testing
print('Test labels shape - y_test.shape: ', y_test.shape)  # labels for testing

classes = [
    'plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship',
    'truck'
]
num_classes = len(classes)
samples_per_class = 7

# for y, cls in enumerate(classes):
# 	idxs = np.flatnonzero(y_train == y)		# returneaza pozitiile pe care gaseste acelasi y_train (numar/label) cu y (cel curent)
# 											# filtrare pe clase. Aici Pozitii = numarul imaginii din X_train

# 	idxs = np.random.choice(idxs, samples_per_class, replace = False)	# alege aleatoriu din arrayul filtrat pe clase
# 																		# 7 elemente pentru display

# 	for i, idx in enumerate(idxs):
# 		plt_idx = i * num_classes + y + 1
# 		plt.subplot(samples_per_class, num_classes, plt_idx)
# 		plt.imshow(X_train[idx].astype('uint8'))
# 		plt.axis('off')
# 		if i == 0:
# 			plt.title(cls)
#plt.show()
# print()

# Subsample the data for more efficient code execution in this exercie
# print('Subsampling')
# print()

# num_training = 5000
# mask = list(range(num_training))
# X_train = X_train[mask]
# y_train = y_train[mask]

# num_test = 1000
# mask = list(range(num_test))
# X_test = X_test[mask]
# y_test = y_test[mask]

# # Reshape image data into rows (every row is an image)
X_train = np.reshape(X_train, (X_train.shape[0], -1))
X_test = np.reshape(X_test, (X_test.shape[0], -1))
print('X_train shape: ', X_train.shape, '\n' + 'X_test shape: ', X_test.shape)

# # Create classifier object
# classifier = KNearestNeighbor()

# classifier.train(X_train, y_train)


# Lets compare how fast the implementations are
def time_function(f, *args):
    """
	Call a function f with args and return the time (in seconds) that it took to execute.
	"""
    import time
    tic = time.time()
    f(*args)
    toc = time.time()
    return toc - tic


# two_loop_time  = time_function(classifier.compute_distances_two_loops,X_test)
# print('Two loop version took %f seconds' % two_loop_time)

# one_loop_time = time_function(classifier.compute_distances_one_loop,X_test)
# print('One loop version took %f seconds' % one_loop_time)

# no_loop_time = time_function(classifier.compute_distances_no_loops,X_test)
# print('No loop version took %f seconds' % no_loop_time)

# dists = classifier.compute_distances_two_loops(X_test)
# print('Dist shape: ', dists.shape)

# # We can visualize the distance matrix: each row is a single test example and
# # its distances to training examples
# plt.imshow(dists, interpolation = 'None')
# plt.show()

# # Now implement the function predict labels
# # Use k = 1 (Which is nearest neighbor)
# y_test_pred = classifier.predict_labels(dists, k=5)

# # Compute and print the fraction of correctly predicted examples
# num_correct = np.sum(y_test_pred == y_test)
# accuracy = float(num_correct) / num_test
# print('Got %d/%d correct => accuracy: %f' %(num_correct, num_test, accuracy))

# # Now lets speed up distance matrix computation by using partial vectorization
# # with one loop. Implement the function compute_distances_one_loop

# dists_one = classifier.compute_distances_one_loop(X_test)
# #print('Dists one: ', dists_one)
# plt.imshow(dists_one, interpolation = 'None')
# plt.show()
# # To ensure that our vectorized implementation is correct, we make sure that it
# # agrees with the naive implementation. There are many ways to decide whether two
# # matrices are similar; one of the simplest is the Frobenius norm. In case you haven't
# # seen it before, the Frobenius norm of two matrices is the square root of the squared
# # sum of differences of all elements; in other words, reshape the matrices into vectors
# # and compute the Euclidian distance between them.

# difference = np.linalg.norm(dists - dists_one, ord = 'fro')

# print('Difference was: %f' % (difference))
# if difference < 0.001:
# 	print('Good! Distance matrices are the same')
# else:
# 	print('Uh-oh! Distance matrices are different')

# # Now implement the full-vectorized version inside compute_distances_no_loops
#dists_two = classifier.compute_distances_no_loops(X_test)

# #check that the distance matrix agrees with the one we computed before:
# difference = np.linalg.norm(dists - dists_two, ord = 'fro')
# print('Difference was: %f' %(difference))
# if difference < 0.001:
# 	print('Good! Distance matrices are the same')
# else:
# 	print('Uh-oh! Distances matrices are different')

# # Set hyperparameters
# num_folds = 5
# k_choices = [1, 3, 5, 8, 10, 12, 15, 20, 50, 100]

# X_train_folds = np.array_split(X_train, num_folds)  # list of arrays
# y_train_folds = np.array_split(y_train, num_folds)

# print()
# print("Train images data-set has %d batches, X_train_folds" %
#       len(X_train_folds))
# print("Train labels data-set has %d batches, y_train_folds" %
#       len(y_train_folds))
# print()
# k_to_accuracies = {}

# # Cross Validation to set hyperparameters
# for hyperk in k_choices:
#     print()
#     print("K:", hyperk)
#     # Iterate over batches of data in the data-set
#     accuracies = []    # list to store all values of accuracy for the current fold
#     for runno in range(len(X_train_folds)):
#         print()
#         print('Iteration', runno)

#         # Build Validation Sets
#         im_validation_set = X_train_folds[runno]  # ndarray
#         # print("image validation set type:", type(im_validation_set))
#         # print("image validation set shape:", im_validation_set.shape)
#         label_validation_set = y_train_folds[runno]  # ndarray
#         # print("label validation set type:", type(im_validation_set))
#         # print("label validation set shape:", label_validation_set.shape)

#         # Build Training Sets
#         im_training_set = X_train_folds[0:runno] + X_train_folds[
#             runno + 1:num_folds]  # list of ndarrays
#         # print("images training set length:", len(im_training_set))
#         # print("Type of im_training_set is:", type(im_training_set))
#         # print("Type of im_training_set elemets is:", type(im_training_set[0]))
#         # print("Shape of im_training_set elemets is:", im_training_set[0].shape)
#         label_training_set = y_train_folds[0:runno] + y_train_folds[runno + 1:num_folds]  # lsit  of ndarrays
#         # print("Type of label_training_set is:", type(im_training_set))
#         # print("Type of label_training_set elemets is:",type(label_training_set[0]))
#         # print("Shape of label_training_set elemets is:",label_training_set[0].shape)
#         # print("labels training length:", len(label_training_set))

#         # Sanity Check to confirm that the validation set is not present in the training set
#         for batch in im_training_set:
#             if np.all(batch == im_validation_set):
#                 print('Fail images')
#         for batch in label_training_set:
#             if np.all(batch == label_validation_set):
#                 print("fail")

#     # Apply KNN algorithm for a number of len(X_train_folds) times for every value of k in k_choices
#     # train the KNearestNeighbor classifier
#     # test set = current validation set
#     # train set = all folds from the dataset except for the validation fold
#     # create ndarray type to store all the elements from im_training_set list in order
#         im_training_set_arr = np.concatenate(im_training_set, axis=0)
#         # print("im_training_set_arr has type:",type(im_training_set_arr))
#         # print("im_training_set_arr has shape:",im_training_set_arr.shape)

#         # create ndarray type to store all the elements from label_training_set list in order
#         label_training_set_arr = np.concatenate(label_training_set, axis=0)

#         classifier.train(im_training_set_arr, label_training_set_arr)
#         dists_two = classifier.compute_distances_no_loops(im_validation_set)
#         # print("Dists_two is of type:", type(dists_two))
#         # print("Dists_two is of shape:", dists_two.shape)
#         y_test_pred = classifier.predict_labels(dists_two, k=hyperk)
#         # print("y_test_pred is of type:", type(y_test_pred))
#         # print("y_test_pred is of shape:", y_test_pred.shape)
#         # print("y_test_pred is:", y_test_pred)

#         # print("y_test is of type:", type(y_test))
#         # print("y_test is of shape:", y_test.shape)
#         # print("y_test is:", y_test)
#         # break
#      # Compute and print the accuracy - fraction of correctly predicted examples

#         num_correct = np.sum(y_test_pred == y_test)
#         # print("Number of correctly predicted photos:", num_correct)
#         accuracy = float(num_correct) / num_test
#         # print("Accuracy:", accuracy)
#         accuracies.append(accuracy)
#     k_to_accuracies[hyperk] = accuracies
# print()
# # Print computed accuracies
# for k in sorted(k_to_accuracies):
#     for accuracy in k_to_accuracies[k]:
#         print('k = %d, accuracy = %f' % (k, accuracy))

# # Plot raw observation
# for k in k_choices:
#         accuracies = k_to_accuracies[k]
#         plt.scatter([k] * len(accuracies), accuracies)

# # Plot the trend with error bars that correspond to standard deviation
# accuracies_mean = np.array([np.mean(v) for k, v in sorted(k_to_accuracies.items())])   # compute mean value of accuracies accross k_to_accuracies
# accuracies_std = np.array([np.std(v) for k, v in sorted(k_to_accuracies.items())])  # compute standard deviation (spread of distrobution) for the flattened array
# plt.errorbar(k_choices, accuracies_mean, yerr = accuracies_std)
# plt.title("Cross validation on k")
# plt.xlabel("k")
# plt.ylabel("Cross validation accuracy")
# plt.show()

# Base on the cross validation results above, choose the best value for k,
# retrain the classifier using all the training data, and test it on the test
# data. You should be able to get above 28% accuracy on the test data
best_k = 7

classifier = KNearestNeighbor()
X_train_raw = np.reshape(X_train_raw, (X_train_raw.shape[0], -1))
X_test_raw = np.reshape(X_test_raw, (X_test_raw.shape[0], -1))
classifier.train(X_train_raw, y_train_raw)
print("Shape of test data-set,", X_test_raw.shape)
y_test_pred = classifier.predict(X_test_raw, k=best_k, num_loops=0)

# Compute and display the accuracy
num_correct = np.sum(y_test_pred == y_test_raw)
accuracy = float(num_correct) / len(X_test_raw)
print("Got %d / %d correct => accuracy: %f" %
      (num_correct, len(X_test_raw), accuracy))
