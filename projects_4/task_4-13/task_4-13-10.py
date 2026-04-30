# Начало
# Ввод размера массива
N = int(input("Введите размер массива N: "))

# Проверка на пустой массив
if N < 1:
    print("Ошибка: массив пуст")
else:
    # sum = 0
    total_sum = 0

    # i = 1
    i = 1

    # Цикл: пока i <= N
    while i <= N:
        # Ввод arr[i]
        arr_i = float(input(f"Введите arr[{i}]: "))

        # Проверка: i нечёт? (i % 2 != 0)
        if i % 2 != 0:
            # sum = sum + arr[i]
            total_sum = total_sum + arr_i

        # i = i + 1
        i = i + 1

    # Вывод результата
    print("Сумма элементов с нечётными индексами:", total_sum)

# Конец