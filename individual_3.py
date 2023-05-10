#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input('Введите слово: ')
    result = ''
    for i in word:
        if i != 'c' and i != 'с':
            result += i
    print(result)
  

delet_c()
