import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def check_if_end(sign):
    if check_if_win(sign):
        return [True, sign + ' wins']
    elif check_if_draw():
        return [True, 'draw']
    return [False]


def game():
    print_board()
    while True:
        player_move()
        print_board()
        if (check_if_end('X'))[0]:
            print(check_if_end('X')[1])
            break
        computer_move()
        print_board()
        if (check_if_end('O'))[0]:
            print(check_if_end('O')[1])
            break


def player_move():
    print('Enter the coordinates: ')
    while True:
        move = input()
        if len(move.split(" ")) < 2:
            print('You should enter numbers!')
        elif not is_move_number(move):
            print('You should enter numbers!')
        elif not is_move_on_board(move):
            print('Coordinates should be from 1 to 3!')
        elif not move_is_available(int(move[0]) - 1, int(move[2]) - 1):
            print('This cell is occupied! Choose another one!')
        else:
            put_move_on_board(int(move[0]) - 1, int(move[2]) - 1, 'X')
            return False


def move_is_available(row, column):
    global board
    return board[row][column] == ' '


def computer_move():
    row_coordinate = random.randint(0, 2)
    column_coordinate = random.randint(0, 2)
    while not move_is_available(row_coordinate, column_coordinate):
        row_coordinate = random.randint(0, 2)
        column_coordinate = random.randint(0, 2)
    print('Making move level "easy"')
    put_move_on_board(row_coordinate, column_coordinate, 'O')


def put_move_on_board(row, column, sign):
    global board
    board[row][column] = sign


def is_move_number(move):
    row = move.split(" ")[0]
    column = move.split(" ")[1]
    return row.isdigit() and column.isdigit()


def is_move_on_board(move):
    return (int(move.split(" ")[0]) in [1, 2, 3] and
            int(move.split(" ")[1]) in [1, 2, 3])


def check_if_occupied(move):
    row = int(move[0])
    column = int(move[2])
    return board[row - 1][column - 1] == ' '


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
    return sum(sign.count(' ') for sign in board) == 0


def vertical(sign):
    global board
    for i in range(3):
        if [item[i] for item in board].count(sign) == 3:
            return True
    return False


def horizontal(sign):
    global board
    for i in range(3):
        if board[i].count(sign) == 3:
            return True
    return False


def diagonal(sign):
    global board
    if (board[0][0] == sign and
            board[1][1] == sign and
            board[2][2] == sign):
        return True
    elif (board[0][2] == sign and
            board[1][1] == sign and
            board[2][0] == sign):
        return True
    return False


def check_if_win(sign):
    return vertical(sign) or horizontal(sign) or diagonal(sign)


game()