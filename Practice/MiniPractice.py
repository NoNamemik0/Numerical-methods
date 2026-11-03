import math

def relative_error(approx, exact):
    if exact == 0:
        return 0.0 if approx == 0 else float('inf')
    return abs(approx - exact) / abs(exact)

print("--- 1. Пи и 3.14 ---")
exact_1 = math.pi
approx_1 = 3.14
print("Абсолютная (Delta):", abs(approx_1 - exact_1))
print("Относительная (delta):", relative_error(approx_1, exact_1))

print("\n--- 2. (0.1 + 0.2) и 0.3 ---")
exact_2 = 0.3
approx_2 = 0.1 + 0.2
print("Результат сложения:", approx_2)
print("Абсолютная (Delta):", abs(approx_2 - exact_2))
print("Относительная (delta):", relative_error(approx_2, exact_2))

print("\n--- 3. Миллион 0.1 против math.fsum ---")
exact_3 = math.fsum([0.1] * 1_000_000)

approx_3 = 0.0
for _ in range(1_000_000):
    approx_3 += 0.1

print("Итог fsum (точное):", exact_3)
print("Итог цикла (приближ):", approx_3)
print("Абсолютная (Delta):", abs(approx_3 - exact_3))
print("Относительная (delta):", relative_error(approx_3, exact_3))
