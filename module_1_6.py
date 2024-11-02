#подсчет символов в строке

my_string = input('Введите произвольный текст: ')
print(len(my_string))

#методы строк

print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print('Первый символ строки: ', my_string[0], 'последний символ строки: ', my_string[-1])