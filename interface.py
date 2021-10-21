#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Реализация интерфейса работы с csv форматом

from csvdownloader import CSV_worker
import Core

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

file_not_ok = True
    
while file_not_ok:
    """Пробуем загрузить файл"""
    
    print(
        """
Обработчик CSV файлов
Для загрузки данных из файла "goods" нажмите "Ввод"
Если требуется загрузить данные из другого файла:
введите имя файла и нажмите "Ввод"
        """)
    fl = input()
    if fl == '':
        fl = 'goods'
    cls()
    try:
        data = CSV_worker(filename=fl, delimiter=':')
    except:
        print(f'{fl} - такой файл не найден')
    else:
        file_not_ok = False

menu = 0
try:
    data_observer = Core.ProductList(data.data)
except:
    menu = 7
    print(f'Ошибка создания списка товаров из файла {fl}')
else:
    if data_observer.productlist == []:
        print(f'Данные не были загружены, возможно файл {fl} пуст')
        menu = 7

while menu != 7:
    """Основной цикл интерфейса программы"""

    cls()
    menu = 0
    print(f'{fl} - файл успешно загружен \n')
    print(
        """
Возможные действия с данными:

1. Отобразить список товаров
2. Средняя цена товаров
3. Самый дорогой товар
4. Самый дешевый товар
5. Товар с максимальным количеством
6. Товар с минимальным количеством
7. Выход из программы

Введите нужную цифру и нажмите "Ввод"
        """
        )
    try:
        inp = int(input('Введите команду: '))
    except:
        print('Введите число в диапазоне 1-7')
    else:
        menu = inp
    if menu == 1:
        print(data_observer)
    elif menu == 2:
        print('Средняя цена товаров:')
        print(data_observer.product_midle_price())
    elif menu == 3:
        print('Самый дорогой товар:')
        print(data_observer.most_expensive())
    elif menu == 4:
        print('Самый дешевый товар:')
        print(data_observer.most_cheapest())
    elif menu == 5:
        print('Товар с максимальным количеством:')
        print(data_observer.max_quantity())
    elif menu == 6:   
        print('Товар с минимальным количеством:')
        print(data_observer.min_quantity())
    elif menu == 7:   
        print('Вы вышли, программа прекращает работу')
    input('Нажмите "Ввод" для продолжения ')
    







