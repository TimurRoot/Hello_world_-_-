files = ["seq1", "seq2", "seq3", "seq4"]

# Фиксированная дата взятия образца (можете изменить на любую другую)
sample_date = "_2023_10_05"  # формат: _ГГГГ_ММ_ДД

for name in files:
    new_name = name + sample_date + ".fasta"
    print(f"{new_name}")
