A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
D = float(input("Введите D: "))

min_val = A  # min = A

if B < min_val:
    min_val = B

if C < min_val:  # C < min ?
    min_val = C  # min = C

if D < min_val:  # D < min ?
    min_val = D  # min = D

print("Минимальное число:", min_val)
