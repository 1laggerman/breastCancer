import numpy as np
import pandas as pd

X = pd.DataFrame(np.array([[0, 5, 2, 1], [0, 1, 5, 8], [2, 3, 4, 2]], dtype=float))
print(X)


n_cols = X.shape[1]
k = int(X.size * 0.01)  # Number of values to replace (1% of array size)

# Get the indices of the smallest k values in each column
# smallest_indices = np.argsort(X, axis=0)[1]
# smallest_indeices = np.argsort(X, axis=0)[:2]

smallest_indices = np.array([1, 2, 2, 2])

print(smallest_indices)

# Calculate the threshold value as the smallest value among the selected indices
# threshold = X[smallest_indices, 1]
threshold = X.values[smallest_indices, np.arange(n_cols)]
print(threshold)

print(X < threshold)

# Replace the smallest values in each column with the threshold
# X[smallest_indices] = threshold


# cols = X.shape[1]
# smallest_indices = np.argsort(X, axis=0)[:X.shape[0] * 0.01, np.arange(cols)]
# thresholds = X[smallest_indices[-1, np.arange(cols)]]

# # below_threshold_indices = np.where(X <= thresholds)

# # X[below_threshold_indices] = thresholds[below_threshold_indices[1]]
# print(thresholds)
# print(smallest_indices)
