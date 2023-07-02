import numpy as np

X = np.array([[0, 5, 2, 1], [0, 1, 5, 8], [2, 3, 4, 2], [1 , 2, 3, 4]], dtype=float)
print(X)
threshold = np.percentile(X, 1, axis=0)
threshold = np.median(X, 1, axis=0)

below_threshold_indices = np.where(X <= threshold)

X[below_threshold_indices] = threshold[below_threshold_indices[1]]
print(X)
