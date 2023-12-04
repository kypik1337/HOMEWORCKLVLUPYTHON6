# Задание №5 Добавьте в модуль с загадками функцию, 
# которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, 
# чтобы передать ей все свои загадки
from Zadanie4 import * 
def storage():
    puzzle = {
        'zimoi and letom:': ['el', 'sosna', 'bereza', 'listva'],
        'sidit ded': ['luk', 'lukovka', 'morkovka']
    }
    for puzzle, answer in puzzle.items():
        result = riddle(puzzle, answer)
        print(f'Winner {result}' if result > 0 else 'Noooo WINNER')
        


if __name__ == '__main__':
    storage()






