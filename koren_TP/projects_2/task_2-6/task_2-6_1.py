def check_ph():
    try:

        ph_value = float(input("Введите значение pH (0-14): "))


        if ph_value < 0 or ph_value > 14:
            print("Ошибка! pH должен находиться в диапазоне от 0 до 14.")
            return


        if ph_value < 7:
            environment = "Кислая среда"
        elif ph_value > 7:
            environment = "Щелочная среда"
        else:
            environment = "Нейтральная среда"


        print(f"\nВведённое значение pH: {ph_value}")
        print(f"Характеристика среды: {environment}")

    except ValueError:
        print("Ошибка! Пожалуйста, введите числовое значение.")


if __name__ == "__main__":
    print("=== Определение среды раствора ===")
    check_ph()
