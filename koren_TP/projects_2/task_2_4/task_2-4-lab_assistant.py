 def prepare_solution():
    try:

        volume = float(input("Введите необходимый объем раствора (в мл): "))


        salt_mass = volume * 0.009


        water_volume = volume


        report = f"""ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:

-----------------------

Общий объем: {volume:.2f} мл
Масса соли:  {salt_mass:.2f} г
Объем воды:  {water_volume:.2f} мл"""


        with open("recipe.txt", "w", encoding="utf-8") as file:
            file.write(report)

        print("\nРецепт успешно сохранен в файл recipe.txt")
        print("Содержание рецепта:")
        print(report)

    except ValueError:
        print("Ошибка: введите числовое значение объема!")


if __name__ == "__main__":
    prepare_solution()