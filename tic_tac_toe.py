# Assignment: W01 Prove: Developer.
# Author: Manuel Armando Flores Yáñez

# This is one of the characters that will be printed below each row of the board followed by another character
SEPARATOR_1 = "-"

# This is one of the characters that will be printed below each row of the board preceded by another character
SEPARATOR_2 = "+"

PLAYERS = ["x", "o"]


def fill_board():
    BOARD_SIZE = 3
    board = []
    counter = 1
    for _ in range(BOARD_SIZE):
        horizontal_line = []
        for __ in range(BOARD_SIZE):
            horizontal_line.append(str(counter))
            counter = counter + 1

        board.append(horizontal_line)

    return board


def main():
    board = fill_board()
    start_game(board)


def start_game(board):
    print_board(board)
    greater_number = board[(len(board)-1)][(len(board)-1)]
    toggle_active_player = True

    while True:

        square_available = True

        if toggle_active_player:
            player = PLAYERS[0]
            toggle_active_player = False
        else:
            player = PLAYERS[1]
            toggle_active_player = True

        square = (input(
            f"\n{player}'s turn to choose a square (1-{len(board)}): "))

        squares_marked = 0
        for y in range(len(board)):
            for x in range(len(board)):
                if square == board[y][x]:
                    board[y][x] = player
                    square_available = False
                if board[y][x] in PLAYERS:
                    squares_marked = squares_marked + 1

        game_completed = validate_game_completion(board)

        if game_completed:
            print_board(board)
            print("\nGood game. Thanks for playing!")
            return

        if squares_marked == (len(board) ** 2):
            print_board(board)
            print("\nDraw")
            return

        try:
            if square_available and int(square) >= 1 and int(square) <= int(greater_number):
                print("\nPlease choose an unmarked square")
                toggle_active_player = not toggle_active_player
            elif int(square) < 1 or int(square) > int(greater_number):
                print(f"\nPlease choose a number between 1 and {len(board)}")
                toggle_active_player = not toggle_active_player
        except:
            print(f"\nPlease choose a number between 1 and {len(board)}")

        print_board(board)


def validate_game_completion(board):
    WINNERS = ["xxx", "ooo"]

    # Validate horizontal line
    for y in range(len(board)):
        horizontal_line = ""
        for x in range(len(board)):
            horizontal_line = horizontal_line + board[y][x]
        if horizontal_line.__contains__(WINNERS[0]) or horizontal_line.__contains__(WINNERS[1]):
            return True

    # Validate vertical line
    for y in range(len(board)):
        vertical_line = ""
        for x in range(len(board)):
            vertical_line = vertical_line + board[x][y]
        if vertical_line.__contains__(WINNERS[0]) or vertical_line.__contains__(WINNERS[1]):
            return True

    # Validate diagonal right line
    diagonal_y = 0
    diagonal_x = 0
    diagonal_line = ""
    for index in range(len(board)):
        diagonal_line = diagonal_line + board[diagonal_y][diagonal_x]
        if diagonal_line.__contains__(WINNERS[0]) or diagonal_line.__contains__(WINNERS[1]):
            return True
        diagonal_y = index + 1
        diagonal_x = index + 1
        if diagonal_x >= len(board) or diagonal_y >= len(board):
            break

    # Validate diagonal left line
    diagonal_y = len(board) - 1
    diagonal_x = 0
    diagonal_line = ""
    for index in range(len(board)):
        diagonal_line = diagonal_line + board[diagonal_y][diagonal_x]
        if diagonal_line.__contains__(WINNERS[0]) or diagonal_line.__contains__(WINNERS[1]):
            return True
        diagonal_y = diagonal_y - 1
        diagonal_x = index + 1
        if diagonal_x >= len(board) or diagonal_y < 0:
            break

    return False


def print_board(board):
    # Creates a next line before printing the Board
    print()

    lines = []
    for y in range(len(board)):
        line = ""
        for x in range(len(board)):
            if x == 0:
                line = board[y][x]
            else:
                line = line + "|" + board[y][x]
        lines.append(line)

    underline = create_underline(lines)
    for text in lines:
        print(text)
        print(underline)


def create_underline(lines):
    underline = ""
    toggle = True
    for _ in range(len(lines[0])):
        if toggle:
            underline = underline + SEPARATOR_1
            toggle = False
        else:
            underline = underline + SEPARATOR_2
            toggle = True

    return underline


if __name__ == "__main__":
    main()
