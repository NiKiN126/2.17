#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
        letters = {'а', 'у', 'е', 'о', 'э', 'я', 'и', 'ю', 'ё', 'ы'}
        string = list(input('Введите строку: ').lower())
        count = 0
        for i, slov in enumerate(string):
            if slov in letters:
                count += 1
        print(count)
