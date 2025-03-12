'''Задача 5. Миссия выполнима'''
from math import ceil                              # вызов функции ceil библиотеки math
from math import floor                             # вызов функции floor библиотеки math

height = float(input('Введите высоту (см): '))

height_up = ceil(height)                           # округление вверх
print('Высота вверх:', height_up, 'см')

height_down = floor(height)                        # округление вниз
print('Высота вниз:', height_down, 'см')