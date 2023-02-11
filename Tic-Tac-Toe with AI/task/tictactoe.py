board = [[], [], []]
who_start = 'X'


def make_board():
    print('Enter the cells: ')
    initial_state = input()
    global board
    global who_start
    k = 0
    for i in range(3):
        for j in range(3):
            board[i].append(initial_state[k])
            k += 1
    print_board()
    if initial_state.count('X') > initial_state.count('O'):
        who_start = 'O'


def put_move_on_board(move):
    global board
    global who_start
    row = int(move[0])
    column = int(move[2])
    board[row - 1][column - 1] = who_start


def make_a_move():
    print('Enter the coordinates: ')
    while True:
        move = input()
        if len(move.split(" ")) < 2:
            print('You should enter numbers!')
        elif not is_move_number(move):
            print('You should enter numbers!')
        elif not is_move_on_board(move):
            print('Coordinates should be from 1 to 3!')
        elif not check_if_occupied(move):
            print('This cell is occupied! Choose another one!')
        else:
            put_move_on_board(move)
            return False


def is_move_number(move):
    row = move.split(" ")[0]
    column = move.split(" ")[1]
    return row.isdigit() and column.isdigit()


def is_move_on_board(move):
    return int(move.split(" ")[0]) in [1, 2, 3] and int(move.split(" ")[1]) in [1, 2, 3]


def check_if_occupied(move):
    row = int(move[0])
    column = int(move[2])
    return board[row - 1][column - 1] == '_'


def print_board():
    print('---------')
    for i in range(3):
        print('|', end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print('|')
    print('---------')


def check_if_draw():
    global board
    return sum(sign.count('_') for sign in board) == 0


def vertical():
    global board
    for i in range(3):
        if [item[i] for item in board].count(who_start) == 3:
            return True
    return False


def horizontal():
    global board
    for i in range(3):
        if board[i].count(who_start) == 3:
            return True
    return False


def diagonal():
    global board
    if (board[0][0] == who_start and
            board[1][1] == who_start and
            board[2][2] == who_start):
        return True
    elif (board[0][2] == who_start and
            board[1][1] == who_start and
            board[2][0] == who_start):
        return True
    return False


def check_if_win():
    return vertical() or horizontal() or diagonal()


def end_of_game():
    if check_if_win():
        print(who_start + ' wins')
    elif check_if_draw():
        print('Draw')
    else:
        print('Game not finished')


make_board()
make_a_move()
print_board()
end_of_game()
