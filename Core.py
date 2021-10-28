#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Реализация функционала обработчика csv файлов

class Product:
    """Класс Товар """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)
        
    def __str__(self):
        return (
            f'наименование: {self.name},' +
            f'цена: {self.price}, ' +
            f'количество: {self.quantity}'
                )
        
        
class ProductList:
    """Класс список товаров """
    def __init__(self, productlist):
        if productlist == []:
            raise IndexError('Получен пустой список')
        self.productlist = [Product(i[0], i[1], i[2]) for i in productlist]
        
    def product_midle_price(self):
        """Вычисление средней цены товаров"""
        total_quantity = 0
        total_sum = 0
        for elem in self.productlist:
            total_quantity += elem.quantity
            total_sum += elem.quantity * elem.price
            
        return "%.2f" % (total_sum / total_quantity)
        
    def most_expensive(self):
        """Определение самого дорогого товара"""
        most_exp = self.productlist[0]
        for elem in self.productlist:
            if elem.price > most_exp.price:
                most_exp = elem
        
        return most_exp
        
    def most_cheapest(self):
        """Определение самого дешевого товара"""
        most_cheap = self.productlist[0]
        for elem in self.productlist:
            if elem.price < most_cheap.price:
                most_cheap = elem
                
        return most_cheap
        
    def max_quantity(self):
        """Определение товара с максимальным количеством"""
        maxq = self.productlist[0]
        for elem in self.productlist:
            if elem.quantity > maxq.quantity:
                maxq = elem
                
        return maxq
        
    def min_quantity(self):
        """Определение товара с минимальным количеством"""
        minq = self.productlist[0]
        for elem in self.productlist:
            if elem.quantity < minq.quantity:
                minq = elem
        
        return minq
        
    def __str__(self):
        """Формирование текстового вывода"""
        text = ' Начало списка' + '\n'
        for elem in self.productlist:
            text += elem.__str__() + '\n'
        text += ' Конец списка'
        
        return text


if __name__ == "__main__":
    print('Это файл описания классов для товаров и списка товаров')
    print('Для тестирования программы запускать interface.py')
