import numpy as np


def to_one_hot(y, k=None):
    """
    Compute a one-hot encoding from a vector of integer labels.
    
    Parameters
    ----------
    y : (N, 1) ndarray
        The zero-indexed integer labels to encode.
    k : int, optional
        The number of distinct labels in `y`.
        
    Returns
    -------
    one_hot : (N, k) ndarray
        The one-hot encoding of the labels.
    """
    n = len(y)
    if k is None:
        k = len(np.unique(y))

    one_hot = np.zeros([n, k], dtype=np.uint8)
    one_hot[np.arange(0, n, 1), y.ravel()] = 1
        
    return one_hot