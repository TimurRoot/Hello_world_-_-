def main():
    try:

        total_capsules = int(input("Введите общее количество произведенных капсул: "))


        package_size = int(input("Введите количество капсул в одной упаковке: "))


        full_packages = total_capsules // package_size
        remainder = total_capsules % package_size


        print("\n--- Отчет фасовочного цеха ---")
        print(f"Полных упаковок:\t{full_packages}")
        print(f"Остаток капсул:\t{remainder}")

    except ValueError:
        print("Ошибка! Пожалуйста, введите целые числа.")


if __name__ == "__main__":
    main()