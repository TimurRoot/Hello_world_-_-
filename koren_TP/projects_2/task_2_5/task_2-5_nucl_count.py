

def analyze_dna():

    dna_sequence = input("Введите последовательность ДНК: ").upper()


    nucleotides = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

    for nucleotide in dna_sequence:
        if nucleotide in nucleotides:
            nucleotides[nucleotide] += 1


    total_length = len(dna_sequence)


    percentages = {
        'A': (nucleotides['A'] / total_length) * 100 if total_length > 0 else 0,
        'T': (nucleotides['T'] / total_length) * 100 if total_length > 0 else 0,
        'G': (nucleotides['G'] / total_length) * 100 if total_length > 0 else 0,
        'C': (nucleotides['C'] / total_length) * 100 if total_length > 0 else 0
    }


    print("\n=== Анализ последовательности ДНК ===")
    print(f"\nПоследовательность в верхнем регистре: {dna_sequence}")

    print("\nПодсчёт нуклеотидов:")
    for nuc in ['A', 'T', 'G', 'C']:
        print(f"{nuc}: {nucleotides[nuc]}")

    print(f"\nОбщая длина: {total_length} нуклеотидов")

    print("\nПроцентное содержание:")
    for nuc in ['A', 'T', 'G', 'C']:
        print(f"{nuc}: {percentages[nuc]:.2f}%")


if __name__ == "__main__":
    analyze_dna()
