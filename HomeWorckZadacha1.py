# 2. В модуль с проверкой даты добавьте возможность запуска 
# в терминале с передачей даты на проверку.
# import sys


# def leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# def valid_date(date_str):
#     day, month, year = map(int, date_str.split('.'))
#     if month < 1 or month > 12:
#         return False
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         max_day = 31
#     elif month in [4, 6, 9, 11]:
#         max_day = 30
#     else:
#         max_day = 29 if leap_year(year) else 28
#     return False if day < 1 or day > max_day else year >= 1 and year <= 9999


# if __name__ == '__mane__':
#     if len(sys.argv) !=2:
#         print('Введите данные через "." чтобы дата имела вид 11.11.2023')
#     else :
#         data_str = sys.argv[1]
#     if valid_date(data_str):
#         print(f"{data_str} - такая дата существует")
#     else:
#         print(f"{data_str} - такая дата не существует")



# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно, 
# что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих 
# друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


N = 8
x = []
y = []


def inp():
    for i in range(N):
        new_x, new_y = [int(s) for s in input(f'введите {i + 1} пару чисел на доске 8×8, через пробел:').split()]
        x.append(new_x)
        y.append(new_y)


def check(x1, y1):
    correct = True
    for i in range(N):
        for j in range(i + 1, N):
            if x1[i] == x1[j] or y1[i] == y1[j] or abs(x1[i] - x1[j]) == abs(y1[i] - y1[j]):
                correct = False

    if correct is True:
        return False
    else:
        return True

if __name__ == '__main__':
    inp()
    print(x)
    print(y)


# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных 
# чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный 
# случайные варианты и выведите 4 успешных расстановки.