from sklearn.svm import SVC
import numpy as np
from custom-kernel import gram_mat
from wfi_levenshtein import wfi_levenshtein

# for x in X:
#    print Xw[x]
# this is how we use indices to calculate a custom RBF (Gaussian) string kernel in 'gram_mat'

# dummy data init
X = np.array([[0], [1], [2], [3], [4]])  # array of indices of 'Xw'
Xw = np.array(['bad', 'boy', 'whatcha', 'gonna', 'do'])
y = [1, 1, 1, 0, 0]

X_test = np.array([[0], [1], [2], [3], [4]])
Xw_test = np.array(['good', 'girl', 'whatcha', 'gonna', 'do'])
y_test = [0, 0, 0, 1, 1]

gm = gram_mat(X, X)

clf = SVC(C = 0.1, kernel='precomputed', random_state=1337)
clf.fit(gaussian_kernel(X, X), y)

preds = model.predict(gram_mat(X_test, X))
