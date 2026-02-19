reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))

# 2. Формируем отчётную строку с помощью f-строки
report_line = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."

# 3. Выводим отчёт в консоль
print(report_line)

# 4. Записываем отчёт в файл inventory.txt
with open("inventory.txt", "a", encoding="utf-8") as file:
    file.write(report_line + "\n")