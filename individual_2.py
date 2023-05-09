def initial_letters():
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
