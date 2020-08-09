def print_board(xo):
    """
    Prints the game board. Takes string with X and O as input
    :param xo: string with X and O
    :return: Nothing. Prints the field
    """
    print(f'---------')
    print(f'| {xo[0]} {xo[1]} {xo[2]} |')
    print(f'| {xo[3]} {xo[4]} {xo[5]} |')
    print(f'| {xo[6]} {xo[7]} {xo[8]} |')
    print(f'---------')


def find_position(a, b):
    coordinates = {
        0: {0: 9},
        1: {
            1: 6,
            2: 3,
            3: 0
        },
        2: {
            1: 7,
            2: 4,
            3: 1
        },
        3: {
            1: 8,
            2: 5,
            3: 2
        }
    }
    return coordinates[a][b]


def winner_found(xo):
    """
    Определяем победителя в игре
    :param xo: Строка ХО
    :type xo: string
    :return: Список победителей
    :rtype: list
    """
    winners = []
    wins = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]
    for i in wins:
        if xo[i[0]] == xo[i[1]] == xo[i[2]] != ' ':
            winners.append(xo[i[0]])
    return winners


def field_is_empty(xo, move_place):
    if move_place == 9:
        return False
    if xo[move_place] == ' ':
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


def input_coordinates(xo):
    """
    Запрашиваем у пользователя координаты и проверяем их правильность
    Если место уже занято другим игроком, то спрашиваем снова.

    :param xo: Строка ХО
    :type xo: string
    :return: Номер позиции в строке ХО
    :rtype: int
    """
    a = 0
    b = 0
    correct_input = False
    while not correct_input:
        try:
            a, b = input().split(' ')
            if 1 <= int(a) <= 3:
                if 1 <= int(b) <= 3:
                    correct_input = True
                else:
                    print('Coordinates should be from 1 to 3!')
            else:
                print('Coordinates should be from 1 to 3!')
        except ValueError:
            print('You should enter numbers!')
            continue

    at_position = find_position(int(a), int(b))

    if field_is_empty(xo, at_position):
        return find_position(int(a), int(b))
    else:
        return False


def place_letter(xo, move_place, sign):
    new_str = xo[:move_place] + sign + xo[move_place + 1:]
    return new_str


def make_move(xo, player):
    """
    :param xo: Строка X и O
    :type xo: string
    :param player: Символ X или O
    :type player:
    """
    coord = None
    while not coord:
        coord = input_coordinates(xo)
        if coord == 0:
            break

    if coord is not None:
        return place_letter(xo, coord, player)


# Game logic is built around manipulating string of 9 characters containing "X"s and
# "O"s.
# Allow additional informational messages to be passed
# to console (might be usefull for debugging)
enabled = False

# Show board for the first time in a game
xo = '         '
print_board(xo)

order_X = 'XOXOXOXOX'


for player in order_X:
    xo = make_move(xo, player)
    print_board(xo)
    winner = winner_found(xo)
    if 'X' in winner:
        print('X wins')
        break
    elif 'O' in winner:
        print('O wins')
        break
if len(winner) == 0:
    print('Draw')