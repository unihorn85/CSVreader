#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Реализация функционала работы с csv форматом

import csv

class CSV_worker():
    def __init__(self, filename, delimiter=':'):        
        with open(filename) as f:
            reader = csv.reader(f, delimiter=delimiter)
            pl = []
            for row in reader:
                pl.append(row)
        self.data = pl
            
    def stop(self, filename, data, delimiter=':'):
        with open(filename, 'w') as f:
            writer = csv.writer(f, delimiter)
            for row in data:
                writer.writerow(row)
"""
Возможно понадобиться...                
    def dictr(self, filename, delimiter=':'):        
        with open(filename) as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            pl = []
            for row in reader:
                pl.append(row)
                print(row)
        self.data = pl
"""
