import numpy as np
from wfi_levenshtein import wfi_levenshtein

def gram_mat(X1, X2, sigma=0.1):
    """
    Redefines a basic grammian matrix used in a calculation of RBF (Gaussian) kernel.
    Instead of a dot product (notably, Euclidean distance) calculates Levenshtein distance between two input strings.
    Thus, the RBF kernel implicitly operates with strings and explicitly with indices of the strings.
    Basic RBF is defined as:
        # gram_matrix[i, j] = np.exp(- np.sum(np.power((x1 - x2), 2)) / float(2 * (sigma**2))).
    In the formulae used in the method, 'Xw' is the out-of-function string array.
    :param X1:
        numpy.ndarray
          input list of indices of an explicit numpy.ndarray of strings
    :param X2:
        numpy.ndarray
          input list of indices of an explicit numpy.ndarray of strings
    :param sigma:
        positive float, optional
          sigma value used in a default calculation of RBF (Gaussian) kernel
    :return:
        numpy.ndarray
          redefined grammian matrix of shape (X1.shape[0], X2.shape[0])
    """
    assert isinstance(X1, numpy.ndarray), "Class of 'X1' is not 'numpy.ndarray': %r" % X1.__class__
    assert isinstance(X2, numpy.ndarray), "Class of 'X2' is not 'numpy.ndarray': %r" % X2.__class__
    
    G = np.zeros((X1.shape[0], X2.shape[0]))
    
    for i, x1 in enumerate(X1):
        for j, x2 in enumerate(X2):
            G[i, j] = np.exp(- np.sum(np.power((editdistance.eval(Xw[x1], Xw[x2])), 2)) / float(2 * (sigma**2)))

    return G
    
