board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"
         ]

turn: str = 'X'


def flip_turn():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


def display_board():
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("{} | {} | {}".format(board[6], board[7], board[8]))


def play_game():
    display_board()
    position = int(input("Enter You Position from 1 to 9:"))
    while position > 9 or position < 1:
        print("Your selection was incorrect pls try again.")
        position = int(input("Enter You Position from 1 to 9: "))
    board[position - 1] = turn
    flip_turn()


def check_win():
    global turn
    # check all rows
    if board[0] == turn and board[1] == turn and board[2] == turn:
        return True
    if board[3] == turn and board[4] == turn and board[5] == turn:
        return True
    if board[6] == turn and board[7] == turn and board[8] == turn:
        return True
    # check all columns
    if board[0] == turn and board[3] == turn and board[6] == turn:
        return True
    if board[1] == turn and board[4] == turn and board[7] == turn:
        return True
    if board[2] == turn and board[5] == turn and board[8] == turn:
        return True
    # check all diagonals
    if board[0] == turn and board[4] == turn and board[8] == turn:
        return True
    if board[2] == turn and board[4] == turn and board[6] == turn:
        return True
    return False


def main():
    n = 9
    while n > 0:
        if check_win():
            print("Player with turn:{} has won the match".format(turn))
            return
        play_game()


main()
