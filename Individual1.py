#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Goods (товар). В классе должны быть представлены поля: наименование
# товара, дата оформления, цена товара, количество единиц товара, номер накладной, по
# которой товар поступил на склад. Реализовать методы изменения цены товара, изменения
# количества товара (увеличения и уменьшения), вычисления стоимости товара

import math


class Goods:

    def __init__(self):
        self.__coast = 0
        self.__date = 0
        self.__name = 0
        self.__quan = 0
        self.__number = 0

    def read(self, name, quan, date, coast, number):
        self.name(name)
        self.quan(quan)
        self.date(date)
        self.coast(coast)
        self.number(number)

    def name(self, prompt=None):
        self.__name = input() if prompt is None else input(prompt)

    def date(self, prompt=None):
        self.__date = input() if prompt is None else input(prompt)

    def coast(self, prompt=None):
        self.__coast = int(input()) if prompt is None else input(prompt)

    def quan(self, prompt=None):
        self.__quan = int(input()) if prompt is None else input(prompt)

    def number(self, prompt=None):
        self.__number = input() if prompt is None else input(prompt)

    def set_coast(self, a):
        self.__coast = a

    def set_quan(self, a):
        self.__quan = a

    def get_info(self):
        return self.__coast, self.__date, self.__name, self.__quan, self.__number

    def __stiom(self):
        return int(self.__coast) * int(self.__quan)

    def dispaly(self):
        print("Наименование товара: {}; "
              "Дата оформления - {}; "
              "Цена товара - {};"
              "Количество единиц товара - {}; "
              "Номер накладной - {}."
              "Стоимость всего товара - {}".format(self.__name, self.__date, self.__coast, self.__quan, self.__number,
                                                   self.__stiom()
                                                   )
              )


if __name__ == '__main__':
    T1 = Goods()
    T1.read("Введите названия ",
            "Введите количество товара ",
            "Введите дату оформления ",
            "цену товара ",
            " и номер накладной "
            )
    T1.dispaly()
    T1.set_quan(50)
    T1.set_coast(250)
    T1.dispaly()
