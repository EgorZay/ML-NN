# Custom RBF (Gaussian) string kernel

It is know that SVM cannot process string inputs in its default configuration. To overcome that problem there exists different implementations of string kernels that may operate with texts. This kernel is an additional configuration of RBF (Gaussian) kernel with a slight alteration of distance (similarity) calculation. Instead of dot product of digit vectors (Euclidean distance) it evaluates __[Levenshtein](https://github.com/EgorZay/ML-NN/blob/master/custom-string-kernel-svm/wfi_levenshtein.py)__ distance between strings to form a __[grammian matrix](https://github.com/EgorZay/ML-NN/blob/master/custom-string-kernel-svm/custom-kernel.py)__. Such strings are defined out-of-function (thus, explicitly). 

However, the `.fit` method of `SVC` receives not a string array as input (apart from the target variable) but an array of indices that relate to the strings (see __[example](https://github.com/EgorZay/ML-NN/blob/master/custom-string-kernel-svm/example.py)__).

_Still personally debating over square of Levenshtein distance with myself..._

# Machine Learning and Neural Network category

Quick guide Q(^,^Q)


**-** *Use sigmoid neurons with cross-entropy loss*

**-** *With softmax neurons, though, use log-likelihood cost*



The latter is to convert classified outputs to probability outputs. The softmax conversion basically forms probability distribution (see directory) with sum of weights being 1.

...
