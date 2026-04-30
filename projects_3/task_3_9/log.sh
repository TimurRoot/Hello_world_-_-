#!/bin/bash

LOG_FILE="report.log"
EXPECTED_CODE="0"

if [ ! -f "$LOG_FILE" ]; then
    echo "Ошибка: файл '$LOG_FILE' не найден!"
    exit 1
fi

ERROR_CODE=$(head -n1 "$LOG_FILE" | tr -d ' \n\r')

if [ "$ERROR_CODE" = "$EXPECTED_CODE" ]; then
    echo "ОК: код ошибки $ERROR_CODE соответствует ожидаемому."
else
    echo "ОШИБКА: код '$ERROR_CODE' ≠ ожидаемому '$EXPECTED_CODE'."
    exit 1
fi
