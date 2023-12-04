from random import randint

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
    print(guess())
        


