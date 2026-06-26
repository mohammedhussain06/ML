import numpy as np

vector = np.array([3,4])

# L2 Normalization

norm = np.linalg.norm(vector)

normalized = vector / norm

print("Original :", vector)

print("Norm :", norm)

print("Normalized :", normalized)

print(np.linalg.norm(normalized))