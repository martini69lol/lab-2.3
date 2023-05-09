def delet_c():
    word = input('Введите слово: ')
    result = ''
    for i in word:
        if i != 'c' and i != 'с':
            result += i
    print(result)
  

delet_c()
