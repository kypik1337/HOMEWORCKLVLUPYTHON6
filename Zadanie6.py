# Задание №6 Добавьте в модуль с загадками функцию, которая принимает 
# на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания 
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

from random import randint
from Zadanie5 import *
_data = {}





def seve_resut(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn

def show_results():
    res = (puzzle for puzzle, nn in _data.items())
    print(*res, sep='\n')


def storage():
    puzzle = {
        'zimoi and letom:': ['el', 'sosna', 'bereza', 'listva'],
        'sidit ded': ['luk', 'lukovka', 'morkovka']
    }
    for puzzle, answer in puzzle.items():
        result = riddle(puzzle, answer)
        print(f'Winner {result}' if result > 0 else 'Noooo WINNER')
    
        

def riddle(riddle_text: str, answer: list[str], count: int = 3) -> int:
    print(f'Ygodai zagadky: \n {riddle_text}')
    for nn in range(1, count +1):
        ans = input(f' popitka number {nn}: ').lower()
        if ans in answer:
            return nn
    return 0


def guess (lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    number = randint(lower, upper)
    for nn in range(1, count + 1):
        answer = int(input(f'Popitka number:{nn}, add number {lower} - {upper}:= '))
        if answer > number:
            print(f' Iskomoe > number')
        elif answer < number:
            print(f' Iskomoe < number')
        else:
            return True
    return False

if __name__ == '__main__':
    storage()
    show_results()





