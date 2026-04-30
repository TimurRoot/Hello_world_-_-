#!/bin/bash

# Заменяем старый путь к базе данных на новый с использованием альтернативного разделителя |
sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php

echo "Замена пути в settings.php выполнена успешно!"
