import numpy as np
from sorcery import dict_of


def accuracy(y, y_pred):
    return np.count_nonzero(y == y_pred) / y.size


def precision(y, y_pred):
    return np.count_nonzero(y_pred[y]) / np.count_nonzero(y_pred)


def recall(y, y_pred):
    return np.count_nonzero(y_pred[y]) / np.count_nonzero(y)


def f1(y, y_pred):
    return 2 * np.count_nonzero(y_pred[y]) / (np.count_nonzero(y_pred) + np.count_nonzero(y))


metrics = dict_of(accuracy, precision, recall, f1)
