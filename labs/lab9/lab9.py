"""
Name: Maddie Reed
lab9.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    str_boar_pos = str(board[position-1])
    if str_boar_pos.isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    shape = character.strip().lower()
    new_board = str(board[position-1]).replace(str(position), shape)
    return new_board


def winning_game(board):
    for index in range(0, 9, 3):
        if board[index] == board[index+1] == board[index+2]:
            return True
    for index in range(0, 3):
        if board[index] == board[index+3] == board[index+6]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    if winning_game(board):
        return True
    else:
        for position in range(0, 9):
            if not is_legal(board, position):
                print("No moves left: tie")
                return True
            else:
                return False


def get_winner(board):
    if not game_over(board):
        return None
    board_str = " "
    for position in (0, 8):
        board_str = board_str + str(board[position])
    x_num = board_str.count('x')
    o_num = board_str.count('o')
    if x_num > o_num:
        return 'x wins'
    if x_num == o_num:
        return 'o wins'


def play(board):
    while not game_over(board):
        for counter in range(0, 1):
            shapes = ['x', 'o']
            turn = shapes[counter % 2]
            prompt = turn + "'s, choose a position"
            position = eval(input(prompt))
            if is_legal(board, position):
                fill_spot(board, position, turn)
                print_board(board)
            else:
                print("you can't put that there!")


def main():
    print("Enter a position from the board to place an x or o. "
          "3 of the same in a row wins the game.")
    board = build_board()
    print_board(board)
    ans = 'y'
    while ans[0]:
        play(board)
        get_winner(board)
        ans = input("Play again?")


if __name__ == '__main__':
    main()
