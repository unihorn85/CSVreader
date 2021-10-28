#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Реализация интерфейса работы с csv форматом (Tkinter) 
from csvdownloader import CSV_worker
import Core
from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext
import os


PROGRAM_NAME = 'Просмотр CSV'

class CSVreader():
    
    def __init__(self, root):
        self.root = root
        self.root.title(PROGRAM_NAME)
        self.root.geometry('800x600')
        self.init_gui()
        
    def open_file(self):
        try:
            fl = filedialog.askopenfilename()
            if fl == ():
                raise FileNotFoundError
            data = CSV_worker(filename=fl, delimiter=':')
        except FileNotFoundError:
            messagebox.showerror('ошибка файла',
                f'Проблема с загрузкой файла {fl}')
        else:
            try:
                self.data_observer = Core.ProductList(data.data)
            except IndexError:
                messagebox.showerror('ошибка файла',
                    f'Ошибка создания списка товаров из файла {fl}')
            else:
                root.title('{} - {}'.format(os.path.basename(fl),PROGRAM_NAME))
                self.info.delete(1.0, END)
                self.info.insert(1.0, f' Файл {fl} успешно загружен')
                self.statuslabel.configure(text=f'Текущий файл {fl}')
                self.loadbutton.configure(text=f'Загрузить другой файл') 
                
                self.button_show_products.configure(state=NORMAL)
                self.button_product_midle_price.configure(state=NORMAL)
                self.button_most_expensive.configure(state=NORMAL)
                self.button_most_cheapest.configure(state=NORMAL)
                self.button_max_quantity.configure(state=NORMAL)
                self.button_min_quantity.configure(state=NORMAL)
                    
    def show_products(self):
        self.info.delete(1.0, END)
        self.info.insert(1.0, self.data_observer.__str__())
        
    def product_midle_price(self):
        self.info.delete(1.0, END)
        self.info.insert(1.0, str(self.data_observer.product_midle_price()))
        
    def most_expensive(self):
        self.info.delete(1.0, END)
        self.info.insert(1.0, str(self.data_observer.most_expensive()))

    def most_cheapest(self):
        self.info.delete(1.0, END)
        self.info.insert(1.0, str(self.data_observer.most_cheapest()))
        
    def max_quantity(self):
        self.info.delete(1.0, END)
        self.info.insert(1.0, str(self.data_observer.max_quantity()))

    def min_quantity(self):
        self.info.delete(1.0, END)
        self.info.insert(1.0, str(self.data_observer.min_quantity()))
            
    def init_gui(self):
        file_choose = Frame(self.root, relief = 'raised', bd=2)
        file_choose.pack(fill = X)
        
        self.statuslabel = Label(file_choose, text="Выберите файл со списком товаров")
        self.loadbutton = Button(file_choose, text="Выбрать файл", command=self.open_file)
        self.statuslabel.pack()
        self.loadbutton.pack()
        
        button_deck = Frame(self.root, bd=2)
        
        self.button_show_products = Button(button_deck, state=DISABLED,
            text="Вывести записи", command=self.show_products)
        self.button_product_midle_price = Button(button_deck, state=DISABLED,
            text="Средняя цена товаров", command=self.product_midle_price)
        self.button_most_expensive = Button(button_deck, state=DISABLED,
            text="Самый дорогой товар", command=self.most_expensive)
        self.button_most_cheapest = Button(button_deck, state=DISABLED,
            text="Самый дешевый товар", command=self.most_cheapest)
        self.button_max_quantity = Button(button_deck, state=DISABLED,
            text="Товар с максимальным количеством", command=self.max_quantity)
        self.button_min_quantity = Button(button_deck, state=DISABLED,
            text="Товар с минимальным количеством", command=self.min_quantity)
            
        self.button_show_products.grid(column=0, row=0, sticky=W+E)
        self.button_product_midle_price.grid(column=0, row=1, sticky=W+E)
        self.button_most_expensive.grid(column=1, row=0, sticky=W+E)
        self.button_most_cheapest.grid(column=1, row=1, sticky=W+E)
        self.button_max_quantity.grid(column=2, row=0, sticky=W+E)
        self.button_min_quantity.grid(column=2, row=1, sticky=W+E)
        
        button_deck.pack()
        
        self.info = scrolledtext.ScrolledText(self.root, fg="lightgreen", bg='black')
        self.info.pack(expand=1)

if __name__ == '__main__':
    root = Tk()
    CSVreader(root)
    root.mainloop()
