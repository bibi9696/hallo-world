
field = [[''] * 3 for i in range(3)]
count = 0

def check_win(field):
    win_coord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),  ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for coord in win_coord:
        a, b, c = coord

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != '':
            draw()
            print(f'Выиграл {field[a[0]][a[1]]}!')
            return True
    return False
def draw():
    print()
    print("   |  0 |  1 |  2 | ")
    print("-------------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {'   | '.join(row)}   | "
        print(row_str)
        print("-------------------")
    print()



def ask():
    while True:
        coords = input("       Ваш ход: ").split()

        if len(coords) != 2:
            print(" Введите 2 координаты!!! ")
            continue
        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа!!! ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона!')
            continue
        if field[x][y] != "":
            print('Клетка занята!')
            continue
        return x, y


while True:
    count += 1
    draw()

    if count % 2 == 1:
        print('Ходит крестик!!!')
    else:
        print('Ходит нолик!!!')

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if check_win(field):

        break

    if count == 9:
        print('Ничья!')
        break
