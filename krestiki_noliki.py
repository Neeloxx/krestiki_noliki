def greet():
    print(' Приветствуем вас ')
    print('      в игре      ')
    print(' крестики-нолики  ')
    print(' Формат ввода: x,y')
    print(' x - номер строки ')
    print(' y - номер строки ')


def pole():
    print(f"  0 1 2")
    for _ in range(3):
        print(f"{_} {field[0][_]} {field[1][_]} {field[2][_]}")


def zapros():
    while True:
        mesto = input("  Ваш ход:  ").split()
        if len(mesto) != 2:
            print('Введите 2 координаты!')
            continue
        x, y = mesto

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона!')
            continue

        if field[x][y] != " ":
            print('Клетка занята!')
            continue

        return x, y


def check_win():
    win_cond = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cond in win_cond:
        symbols = []
        for c in cond:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X",]:
            print('Выиграл X!')
            return True
        if symbols == ["O", "O", "O",]:
            print('Выиграл O!')
            return True
    return False



greet()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1

    pole()

    if num % 2 == 1:
        print('Ходит крестик:')
    else:
        print('Ходит нолик:')

    x, y = zapros()

    if num % 2 == 1:
        field[x][y] = 'X'

    else:
        field[x][y] = "O"

    if check_win():
        break

    if num == 9:
        print('Ничья')
        break

