seq = [
    "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",
    "CGCGTACGACTAGCTACGATCGATCGTAGCTAGCTAG",
    "TTACGATCGATACGATCGATCGATCGATACGATACGA",
    "GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"
]

for sequence in seq:
    # Выводим последовательность целиком
    print(f"Последовательность целиком: {sequence}")

    print("Построчный вывод:")
    for nucleotide in sequence:
        print(nucleotide)
print("-" * 40)

print("Цикл выполнен")
