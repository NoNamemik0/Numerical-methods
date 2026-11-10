import numpy as np

arr = np.arange(24).reshape(6, 4)

print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

arr_4x6 = arr.reshape(4, 6)
arr_3d = arr.reshape(2, 3, 4)
arr_flat = arr.reshape(24)

print(np.array_equal(arr_flat, np.arange(24)))

col = arr[:, 2]
print(col)

col[0] = 999
print(col)
print(arr)

arr[0, 2] = 2

mask = arr > 10
elements = arr[mask]
print(elements)
print(elements.mean())

row_means = arr.mean(axis=1, keepdims=True)
arr_centered = arr - row_means

print(arr_centered.shape)
print(arr_centered)
print(arr_centered.sum(axis=1))
