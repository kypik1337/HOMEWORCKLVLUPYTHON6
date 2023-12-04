# Задание №4 Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с 
# возможными вариантами отгадок и количество 
# попыток на угадывание. Программа возвращает 
# номер попытки, с которой была отгадана загадка 
# или ноль, если попытки исчерпаны.

def riddle(riddle_text: str, answer: list[str], count: int = 3) -> int:
    print(f'Ygodai zagadky: \n {riddle_text}')
    for nn in range(1, count +1):
        ans = input(f' popitka number {nn}: ').lower()
        if ans in answer:
            return nn
    return 0
if  __name__ == '__main__':
    result = riddle('zimoi and letom: ', ['el', 'sosna', 'bereza', 'listva'])
    print(result)



