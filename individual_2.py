#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input('Введите слово: ')
    result = ''
    for i in word:
        if i != 'c' and i != 'с':
            result += i
    print(result)
    word_1 = input('Введите первое слово: ')
    word_2 = input('Введите второе слово: ')
    result = 0
    k = 0
    for i in word_1:
        if i == word_2[k]:
            result += 1
            k += 1
        else:
            break
    print(result)
    
