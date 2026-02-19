operator_name = input("Введите имя оператора: ").strip()
pressure_value = input("Введите текущее значение датчика давления: ").strip()

if not operator_name:
    print("Ошибка: имя оператора не может быть пустым!")
    exit()

if not pressure_value:
    print("Ошибка: значение давления не может быть пустым!")
    exit()

with open("sensor_log.txt", "a", encoding="utf-8") as file:
    # Если файл новый, добавляем заголовок (только один раз)
    if file.tell() == 0:  # проверяем, что файл пустой
        file.write("ОПЕРАТОР\tЗНАЧЕНИЕ\n")

    file.write(f"{operator_name}\t{pressure_value}\n")

print("Данные успешно сохранены в sensor_log.txt")