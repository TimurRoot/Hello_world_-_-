#!/bin/bash

# Выводим заголовок таблицы
printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

# Перебираем все файлы с расширением .fasta
for file in *.fasta; do
    # Пропускаем, если файл не существует (например, нет файлов .fasta в папке)
    [ ! -e "$file" ] && continue

    # Пропускаем пустые файлы (0 байт)
    if [ ! -s "$file" ]; then
        continue
    fi

    # Извлекаем последовательности (исключаем строки с >), объединяем в одну строку
    sequence=$(grep -v "^>" "$file" | tr -d '\n')

    # Подсчитываем количество нуклеотидов
    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)

    # Выводим строку таблицы для текущего файла
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done

