import numpy as np
from random import shuffle
#from past.builtins import range

def svm_loss_naive(W, X, y, reg):
    """
  Structured SVM loss function, naive implementation (with loops).

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
    dW = np.zeros(W.shape) # initialize the gradient as zero
    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in range(num_train):
        # Compute scores for one image (every pixel in the image)
        scores = X[i].dot(W)           # Scores shape = (10,)
        correct_class_score = scores[y[i]]  # y[i] = label for image X[i]
        for j in range(num_classes):
            if j == y[i]:
                continue
            margin = scores[j] - correct_class_score + 1 # note delta = 1
            if margin > 0:
                loss += margin
                dW[:, y[i]] -= X[i]
                dW[:, j] += X[i]

    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead so we divide by num_train.
    loss /= num_train
    dW = dW / num_train

    # Add regularization to the loss.
    loss += 0.5 * reg * np.sum(W * W)
    dW += reg * W

    #############################################################################
    # TODO:                                                                     #
    # Compute the gradient of the loss function and store it dW.                #
    # Rather that first computing the loss and then computing the derivative,   #
    # it may be simpler to compute the derivative at the same time that the     #
    # loss is being computed. As a result you may need to modify some of the    #
    # code above to compute the gradient.                                       #
    #############################################################################


    return loss, dW


def svm_loss_vectorized(W, X, y, reg):
    """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as svm_loss_naive.
  """
    loss = 0.0
    dW = np.zeros(W.shape) # initialize the gradient as zero
    num_train = X.shape[0]  # rows/images = 500
    delta = 1
    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the structured SVM loss, storing the    #
    # result in loss.                                                           #
    #############################################################################
    scores = X.dot(W)   # 500x3073 * 3073x10 => shape = (500,10)
    yi_scores = scores[np.arange(scores.shape[0]), y]   # scores for the correct class shape = (500,)
    margins = np.maximum(0, scores - np.matrix(yi_scores).T + delta)    # subtract the column vector np.matrix(yi_scores).T from the scores matrix
    # print("\nMargins shape:", margins.shape)
    margins[np.arange(num_train), y] = 0      # set the margin for the correct class to 0
    loss = np.mean(np.sum(margins, axis = 1))   # compute mean of the rowise sum (aka the average loss over all exameples)
    loss += 0.5 * reg * np.sum(W*W)   # add regularization to the loss function

    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################


    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the gradient for the structured SVM     #
    # loss, storing the result in dW.                                           #
    #                                                                           #
    # Hint: Instead of computing the gradient from scratch, it may be easier    #
    # to reuse some of the intermediate values that you used to compute the     #
    # loss.                                                                     #
    #############################################################################
    binary = margins    # shape = (500,10)
    binary[margins>0] = 1   # set to 1 any value in binary and margins that sattisfies the condition in brackets
    row_sum = np.sum(binary, axis = 1)  # shape = (500,)
    binary[np.arange(num_train), y] = -row_sum.T  # binary = (500,10), row_sum.T = (1,500)
    dW = np.dot(X.T, binary)

    # Average
    dW /= num_train

    # Regularize
    dW += reg * W
    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################

    return loss, dW
