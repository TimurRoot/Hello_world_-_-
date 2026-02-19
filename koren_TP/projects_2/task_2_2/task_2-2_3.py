# Инициализация переменных в стиле snake_case
device_name = "Ноутбук ПВК‑234"
inventory_number = "ПВК‑234"
is_working = True  # True означает «исправен»
quantity = 1

# Вывод таблицы с использованием табуляции
print("Название прибора\t\tИнвентарный номер\t\tСостояние\t\tКоличество")
print(f"{device_name}\t\t{inventory_number}\t\t{'Исправен' if is_working else 'Неисправен'}\t\t{quantity}")