# Ввод числа N
N = int(input("Введите N: "))

# Начальная инициализация
factorial = 1
i = 1

# Цикл: пока i <= N
while i <= N:
    factorial = factorial * i  # factorial *= i
    i = i + 1                  # i += 1

# Вывод результата
print(f"{N}! = {factorial}")