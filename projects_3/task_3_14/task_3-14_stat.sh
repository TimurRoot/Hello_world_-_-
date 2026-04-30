#!/bin/bash

echo "=== Статистика по оценкам студентов ==="

# Находим сумму всех оценок
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма всех оценок: $sum"

# Находим среднюю оценку
avg=$(awk '{sum += $2; count++} END {if (count > 0) print sum / count; else print 0}' students.txt)
printf "Средняя оценка: %.2f\n" "$avg"

# Находим максимальную оценку
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)
echo "Максимальная оценка: $max"
