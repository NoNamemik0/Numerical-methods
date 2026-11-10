print("Задание 1")
#Задание 1

import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_sum(arr):
    total = 0.0
    for x in arr:
        total += x
    return total

def numpy_sum(arr):
    return arr.sum()

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_sum, a)
r_numpy, t_numpy = measure(numpy_sum, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")

print("Задание 2")
#Задание 2

import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_stats(arr):
    n = len(arr)
    s = 0.0
    s2 = 0.0
    for x in arr:
        s += x
        s2 += x * x
    mean = s / n
    std = (s2 / n - mean**2) ** 0.5
    return mean, std

def numpy_stats(arr):
    return arr.mean(), arr.std()

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_stats, a)
r_numpy, t_numpy = measure(numpy_stats, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy, atol=1e-12)}")

print("Задание 3")
#Задание 3

import math
import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_calc(arr):
    result = []
    for x in arr:
        result.append(math.sin(x) + x * x)
    return result

def numpy_calc(arr):
    return np.sin(arr) + arr**2

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_calc, a)
r_numpy, t_numpy = measure(numpy_calc, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

print("Задание 4")
#Задание 4

import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_clip(arr):
    result = arr.copy()
    for i in range(len(result)):
        if result[i] < 0:
            result[i] = 0
        elif result[i] > 1:
            result[i] = 1
    return result

def numpy_clip(arr):
    return np.clip(arr, 0, 1)

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_clip, a)
r_numpy, t_numpy = measure(numpy_clip, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

print("Задание 5")
#Задание 5

import time
import numpy as np

rng = np.random.default_rng(42)
m = rng.normal(size=(100_000, 10))

def loop_sum_rows(mat):
    result = [0.0] * mat.shape[0]
    for i in range(mat.shape[0]):
        s = 0.0
        for j in range(mat.shape[1]):
            s += mat[i, j]
        result[i] = s
    return result

def numpy_sum_rows(mat):
    return mat.sum(axis=1)

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_sum_rows, m)
r_numpy, t_numpy = measure(numpy_sum_rows, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

print("Задание 6")
#Задание 6

import time
import numpy as np

rng = np.random.default_rng(42)
m = rng.normal(size=(100_000, 10))

def loop_normalize(mat):
    result = mat.copy()
    for j in range(mat.shape[1]):
        s = 0.0
        for i in range(mat.shape[0]):
            s += mat[i, j]
        col_mean = s / mat.shape[0]
        for i in range(mat.shape[0]):
            result[i, j] -= col_mean
    return result

def numpy_normalize(mat):
    return mat - mat.mean(axis=0)

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_normalize, m)
r_numpy, t_numpy = measure(numpy_normalize, m)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

print("Задание 7")
#Задание 7

import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_max(arr):
    max_val = arr[0]
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    return max_val, max_idx

def numpy_max(arr):
    return arr.max(), arr.argmax()

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_max, a)
r_numpy, t_numpy = measure(numpy_max, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {r_loop == r_numpy}")

print("Задание 8")
#Задание 8

import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_filter(arr):
    return [x for x in arr if x > 0]

def numpy_filter(arr):
    return arr[arr > 0]

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_filter, a)
r_numpy, t_numpy = measure(numpy_filter, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

print("Задание 9")
#Задание 9

import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_inplace_abs(arr):
    result = arr.copy()
    for i in range(len(result)):
        if result[i] < 0:
            result[i] = -result[i]
    return result

def numpy_inplace_abs(arr):
    result = arr.copy()
    result[result < 0] *= -1
    return result

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_inplace_abs, a)
r_numpy, t_numpy = measure(numpy_inplace_abs, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

print("Задание 10")
#Задание 10

import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

def loop_combined(arr):
    return [x for x in arr if -1 < x < 1]

def numpy_combined(arr):
    return arr[(arr > -1) & (arr < 1)]

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_combined, a)
r_numpy, t_numpy = measure(numpy_combined, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

print("Задание 11")
#Задание 11

import time
import numpy as np

rng = np.random.default_rng(42)
X = rng.normal(size=(1000, 3))
Y = rng.normal(size=(1000, 3))

def loop_dist(data):
    mat_x, mat_y = data
    n = mat_x.shape[0]
    m = mat_y.shape[0]
    result = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            dist = 0.0
            for k in range(3):
                dist += (mat_x[i, k] - mat_y[j, k]) ** 2
            result[i, j] = dist**0.5
    return result

def numpy_dist(data):
    mat_x, mat_y = data
    return np.sqrt(((mat_x[:, None, :] - mat_y[None, :, :]) ** 2).sum(axis=2))

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop, t_loop = measure(loop_dist, (X, Y))
r_numpy, t_numpy = measure(numpy_dist, (X, Y))

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

