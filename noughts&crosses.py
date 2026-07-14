def noughts_crosses():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    gamerunning = True
    while gamerunning == True:
        player_turn = "noughts"

        pick_location("O", "nought", "Player 1", board)

        if check_winner(board, player_turn):
            gamerunning = False
            break

        if check_draw(board):
            gamerunning = False
            break

        player_turn = "crosses"

        pick_location("X", "cross", "Player 2", board)

        if check_winner(board, player_turn):
            gamerunning = False
            break

        if check_draw(board):
            gamerunning = False
            break


def pick_location(symbol, item, player, board):
    repeat = True
    while repeat == True:
        try:
            location = int(input(
                f"\n{player}: Enter the location of where you want to place your chosen {item} (0 to 8 on a grid (top left rightwards)). \n\n"))
            if location > 8 or location < 0:
                print("Ensure to choose an integer between 0 and 8.")
            elif board[location] == "O" or board[location] == "X":
                print("Try again! This space is already in use.")
            else:
                board[location] = symbol
                print(
                    f"\nThere is now a {item} in position {location}. ")
                show_board(board)
                repeat = False
        except ValueError:
            print("Ensure to choose an integer between 0 and 8.")


def check_winner(board, player_turn):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                            [0, 4, 8], [2, 4, 6]]   # Diagonals
    checkboard = board.copy()
    if player_turn == "noughts":
        for index, noughtcross in enumerate(checkboard):
            if noughtcross == "O":
                checkboard[index] = index
            else:
                checkboard[index] = "PLAYABLE"
    else:
        for index, noughtcross in enumerate(checkboard):
            if noughtcross == "X":
                checkboard[index] = index
            else:
                checkboard[index] = "PLAYABLE"

    counter = 0
    for combination in winning_combinations:
        counter = 0
        for single in combination:
            if checkboard[single] == single:
                counter += 1
        if counter == 3:
            print(f"The winner is {player_turn}!")
            return True
    return False


def show_board(board):
    display = []
    for box in board:
        if box == "O":
            display.append("O")
        elif box == "X":
            display.append("X")
        else:
            display.append(" ")
    print("\nCurrent Board:")
    print(f"\n{display[0]}  |  {display[1]}  |  {display[2]}")
    print(f"\n{display[3]}  |  {display[4]}  |  {display[5]}")
    print(f"\n{display[6]}  |  {display[7]}  |  {display[8]}\n")


def check_draw(board):
    filled = 0
    for box in board:
        if box != "O" and box != "X":
            continue
        else:
            filled += 1
            if filled == 9:
                print("It is a draw!")
                return True
    return False


noughts_crosses()
