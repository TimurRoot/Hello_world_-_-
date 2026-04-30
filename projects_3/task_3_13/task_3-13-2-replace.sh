#!/bin/bash

# Заменяем пробелы на символы табуляции в файле sequences.txt
sed -i 's/ /\t/g' sequences.txt

echo "Замена пробелов на табуляции в sequences.txt выполнена успешно!"
