#!/bin/bash

# Ищем строку текущего пользователя в файле /etc/passwd
grep "$USER" /etc/passwd
