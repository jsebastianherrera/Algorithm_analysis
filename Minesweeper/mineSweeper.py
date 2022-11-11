import math
import random

ROWS = 10
TRIES = 0
COLUMNS = 10
MINE_COUNT = 10

BOARD = []
MINES = set()
EXTENDED = set()
PSMINES = set()
NOMINES = set()
UNOS = set()
QUEUE = set()

MATRIX = [['?'] * COLUMNS for i in range(ROWS)]


class Colors(object):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


def colorize(s, color):
    return '{}{}{}'.format(color, s, Colors.ENDC)


def get_index(i, j):
    if 0 > i or i >= COLUMNS or 0 > j or j >= ROWS:
        return None
    return i * ROWS + j


def create_board():
    squares = ROWS * COLUMNS

    # Create board
    for _ in range(squares):
        BOARD.append('[ ]')

    # Create mines
    while True:
        if len(MINES) >= MINE_COUNT:
            break
        MINES.add(int(math.floor(random.random() * squares)))


def draw_board():
    lines = []

    for j in range(ROWS):
        if j == 0:
            lines.append('   ' + ''.join(' {} '.format(x)
                         for x in range(COLUMNS)))

        line = [' {} '.format(j)]
        for i in range(COLUMNS):
            line.append(BOARD[get_index(i, j)])
        lines.append(''.join(line))

    return '\n'.join(reversed(lines))


def parse_selection(raw_selection):
    try:
        return [int(x.strip(','), 10) for x in raw_selection.split(' ')]
    except Exception:
        return None


def adjacent_squares(i, j):
    num_mines = 0
    squares_to_check = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue

            coordinates = i + di, j + dj

            # Skip squares off the board
            proposed_index = get_index(*coordinates)
            if not proposed_index:
                continue

            if proposed_index in MINES:
                num_mines += 1

            squares_to_check.append(coordinates)

    return num_mines, squares_to_check


def adjacent_squares_value(i, j):
    num_mines = 0
    squares_to_check = []
    values = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            # Skip current square
            if di == dj == 0:
                continue

            coordinates = i + di, j + dj

            # Skip squares off the board
            proposed_index = get_index(*coordinates)
            if not proposed_index:
                continue

            if proposed_index in MINES:
                num_mines += 1

            squares_to_check.append(coordinates)
            i, j = coordinates
            values.append(MATRIX[i][j])

    return values


def update_board2(square, selected=True):
    i, j = square
    index = get_index(i, j)
    EXTENDED.add(index)
    if index in MINES:
        return True
    else:
        return


def update_board(square, selected=True):
    i, j = square
    index = get_index(i, j)
    EXTENDED.add(index)

    if index in MINES:
        if not selected:
            return
        BOARD[index] = colorize(' X ', Colors.RED)
        return True
    else:
        num_mines, squares = adjacent_squares(i, j)
        MATRIX[i][j] = num_mines
        if num_mines:
            if num_mines == 1:
                text = colorize(num_mines, Colors.BLUE)
            elif num_mines == 2:
                text = colorize(num_mines, Colors.GREEN)
            else:
                text = colorize(num_mines, Colors.RED)

            BOARD[index] = ' {} '.format(text)
            return
        else:
            BOARD[index] = '   '

            for asquare in squares:
                aindex = get_index(*asquare)
                if aindex in EXTENDED:
                    continue
                EXTENDED.add(aindex)
                update_board(asquare, False)


def reveal_mines():
    for index in MINES:
        if index in EXTENDED:
            continue
        BOARD[index] = colorize(' X ', Colors.YELLOW)


def has_won():
    return len(EXTENDED | MINES) == len(BOARD)

# JUGADORES


def random_player():
    options = []
    for i in range(ROWS):
        for j in range(COLUMNS):
            if MATRIX[i][j] == '?':
                options.append((i, j))
    rand_square = options[random.randint(0, len(options)-1)]
    return rand_square


def heuristic_player():
    ONE = []

    for i in range(ROWS):
        for j in range(COLUMNS):
            cont = 0
            ind = 0
            if MATRIX[i][j] == 1:
                if j+1 <= COLUMNS-1:
                    if MATRIX[i][j+1] == '?':
                        cont = cont + 1
                        ind = i, j+1
                if j-1 >= 0:
                    if MATRIX[i][j-1] == '?':
                        cont = cont + 1
                        ind = i, j-1
                if i+1 <= ROWS-1:
                    if MATRIX[i+1][j] == '?':
                        cont = cont + 1
                        ind = i+1, j
                if i-1 >= 0:
                    if MATRIX[i-1][j] == '?':
                        cont = cont + 1
                        ind = i-1, j
                if i-1 >= 0 and j+1 <= COLUMNS-1:
                    if MATRIX[i-1][j+1] == '?':
                        cont = cont + 1
                        ind = i-1, j+1
                if i+1 <= ROWS-1 and j+1 <= COLUMNS-1:
                    if MATRIX[i+1][j+1] == '?':
                        cont = cont + 1
                        ind = i+1, j+1
                if j-1 >= 0 and i+1 <= ROWS-1:
                    if MATRIX[i+1][j-1] == '?':
                        cont = cont + 1
                        ind = i+1, j-1
                if i-1 >= 0 and j-1 >= 0:
                    if MATRIX[i-1][j-1] == '?':
                        cont = cont + 1
                        ind = i-1, j-1
            if cont != 0:
                # print(cont)
                if cont == 1:
                    PSMINES.add(ind)
    for k in PSMINES:
        i, j = k
        subOne = []
        if j+1 <= COLUMNS-1:
            if MATRIX[i][j+1] == 1:
                ind = i, j+1
                subOne.append(ind)
        if j-1 >= 0:
            if MATRIX[i][j-1] == 1:
                ind = i, j-1
                subOne.append(ind)
        if i+1 <= ROWS-1:
            if MATRIX[i+1][j] == 1:
                ind = i+1, j
                subOne.append(ind)
        if i-1 >= 0:
            if MATRIX[i-1][j] == 1:
                ind = i-1, j
                subOne.append(ind)
        if i-1 >= 0 and j+1 <= COLUMNS-1:
            if MATRIX[i-1][j+1] == 1:
                ind = i-1, j+1
                subOne.append(ind)
        if i+1 <= ROWS-1 and j+1 <= COLUMNS-1:
            if MATRIX[i+1][j+1] == 1:
                ind = i+1, j+1
                subOne.append(ind)
        if j-1 >= 0 and i+1 <= ROWS-1:
            if MATRIX[i+1][j-1] == 1:
                ind = i+1, j-1
                subOne.append(ind)
        if i-1 >= 0 and j-1 >= 0:
            if MATRIX[i-1][j-1] == 1:
                ind = i-1, j-1
                subOne.append(ind)
        ONE.append(subOne)
    for l in ONE:
        for m in l:
            i, j = m
            if j+1 <= COLUMNS-1:
                if MATRIX[i][j+1] == '?':
                    if (i, j+1) not in PSMINES:
                        NOMINES.add((i, j+1))

            if j-1 >= 0:
                if MATRIX[i][j-1] == '?':
                    if (i, j-1) not in PSMINES:
                        NOMINES.add((i, j-1))
            if i+1 <= ROWS-1:
                if MATRIX[i+1][j] == '?':
                    if (i+1, j) not in PSMINES:
                        NOMINES.add((i+1, j))
            if i-1 >= 0:
                if MATRIX[i-1][j] == '?':
                    if (i-1, j) not in PSMINES:
                        NOMINES.add((i-1, j))
            if i-1 >= 0 and j+1 <= COLUMNS-1:
                if MATRIX[i-1][j+1] == '?':
                    if (i-1, j+1) not in PSMINES:
                        NOMINES.add((i-1, j+1))
            if i+1 <= ROWS-1 and j+1 <= COLUMNS-1:
                if MATRIX[i+1][j+1] == '?':
                    if (i+1, j+1) not in PSMINES:
                        NOMINES.add((i+1, j+1))
            if j-1 >= 0 and i+1 <= ROWS-1:
                if MATRIX[i+1][j-1] == '?':
                    if (i+1, j-1) not in PSMINES:
                        NOMINES.add((i+1, j-1))
            if i-1 >= 0 and j-1 >= 0:
                if MATRIX[i-1][j-1] == '?':
                    ind = i-1, j-1
                    if (i-1, j-1) not in PSMINES:
                        NOMINES.add((i-1, j-1))


def SmartPlayer(trie):
    heuristic_player()
    if trie == 0:
        return random_player()
    if len(NOMINES) != 0:
        return NOMINES.pop()
    else:
        while True:
            square = random_player()
            if square not in PSMINES:
                return square


if __name__ == '__main__':
    create_board()
    trie = 0
    while True:

        print(draw_board())
        square = SmartPlayer(trie)
        trie = trie + 1
        if not square or len(square) < 2:
            print('Unable to parse indicies, try again...')
            continue

        mine_hit = update_board(square)

        if mine_hit or has_won():
            if mine_hit:
                reveal_mines()
                print(draw_board())
                print('Game over')
            else:
                print(draw_board())
                print('You won!')
            break
