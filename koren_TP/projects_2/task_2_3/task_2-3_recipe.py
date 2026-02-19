medium_name = input("Введите название питательной среды: ").strip()
agar_concentration = input("Введите концентрацию агара (%): ").strip()
sterilization_temp = input("Введите температуру стерилизации (°C): ").strip()

with open("recipe.txt", "w", encoding="utf-8") as file:

    file.write(f"{medium_name}\n")
    file.write("-" * len(medium_name) + "\n\n")

    file.write("Параметры приготовления:\n")
    file.write(f"  • Концентрация агара: {agar_concentration}%\n")
    file.write(f"  • Температура стерилизации: {sterilization_temp}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")