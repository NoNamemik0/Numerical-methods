import math
import mpmath

mpmath.mp.dps = 50

def relative_error(approx, exact):
    return abs(approx - exact) / abs(exact)

def f_bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)

def f_good(x):
    return 1.0 / (math.sqrt(x + 1) + math.sqrt(x))

def f_exact(x):
    x_mp = mpmath.mpf(x)
    return float(mpmath.sqrt(x_mp + 1) - mpmath.sqrt(x_mp))

xs = [10**10, 10**12, 10**14]

print(f"{'x':<7} | {'Плохой способ':<15} | {'Хороший способ':<15} | {'Ошибка bad':<10} | {'Ошибка good':<10}")
print("-" * 70)

for x in xs:
    bad_res = f_bad(x)
    good_res = f_good(x)
    exact_res = f_exact(x)
    
    err_bad = relative_error(bad_res, exact_res)
    err_good = relative_error(good_res, exact_res)

    print(f"1e+{int(math.log10(x)):<2} | {bad_res:<15.12f} | {good_res:<15.12f} | {err_bad:<10.2e} | {err_good:<10.2e}")
