#!/bin/bash

read -p "Масса (кг): " w
read -p "Рост (м): " h

bmi=$(echo "scale=0; $w / ($h * $h)" | bc -l)

echo "ИМТ: $bmi"
