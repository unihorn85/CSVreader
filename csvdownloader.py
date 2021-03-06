#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Реализация функционала работы с csv форматом

import csv

class CSV_worker():
    """Класс для работы с файлами csv формата"""
    # Пока реализован только необходимый функционал
    def __init__(self, filename, delimiter=':'):        
        with open(filename) as f:
            reader = csv.reader(f, delimiter=delimiter)
            pl = []
            for row in reader:
                pl.append(row)
        self.data = pl
            
    def save(self, filename, data, delimiter=':'):
        with open(filename, 'w') as f:
            writer = csv.writer(f, delimiter)
            for row in data:
                writer.writerow(row)
                

if __name__ == "__main__":
    print('Это файл описания класса работы с csv')
    print('Для тестирования программы запускать interface.py')
