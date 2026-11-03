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

print("Результаты лабораторного эксперимента:")
for x in xs:
    bad_res = f_bad(x)
    good_res = f_good(x)
    exact_res = f_exact(x)
    
    print(f"\nПри x = {x}:")
    print(f"  Плохой способ:   {bad_res:.12f}")
    print(f"  Хороший способ:  {good_res:.12f}")
    print(f"  Эталон (mpmath): {exact_res:.12f}")
    print(f"  -> Относительная ошибка ПЛОХОГО: {relative_error(bad_res, exact_res)}")
    print(f"  -> Относительная ошибка ХОРОШЕГО: {relative_error(good_res, exact_res)}")
