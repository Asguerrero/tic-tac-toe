from math import inf as infinity

triqui = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_board(triqui):
    print('----------------')
    print('| ' + str(triqui[0][0]) + ' || ' + str(triqui[0][1]) + ' || ' + str(triqui[0][2]) + ' |')
    print('----------------')
    print('| ' + str(triqui[1][0]) + ' || ' + str(triqui[1][1]) + ' || ' + str(triqui[1][2]) + ' |')
    print('----------------')
    print('| ' + str(triqui[2][0]) + ' || ' + str(triqui[2][1]) + ' || ' + str(triqui[2][2]) + ' |')
    print('----------------')


def check_winner(triqui):
    finished = False
    coordinates = None

    # Check lines
    for x in range(3):
        if triqui[x][0] == triqui[x][1] and triqui[x][0] == triqui[x][2] and triqui[x][0] != " ":
            finished = True
            coordinates = triqui[x][0]

            # Check columns
    for y in range(3):
        if triqui[0][y] == triqui[1][y] and triqui[0][y] == triqui[2][y] and triqui[0][y] != " ":
            finished = True
            coordinates = triqui[0][y]

    # Check diagonals
    if triqui[0][0] == triqui[1][1] and triqui[0][0] == triqui[2][2] and triqui[0][0] != " ":
        finished = True
        coordinates = triqui[0][0]

    if triqui[0][2] == triqui[1][1] and triqui[0][2] == triqui[2][0] and triqui[0][0] != " ":
        finished = True
        coordinates = triqui[0][2]

    empty = False
    # Check for empty cells
    for x in range(3):
        for y in range(3):
            if triqui[x][y] == " ":
                empty = True

    if not empty:
        finished = True
        if coordinates is None:
            return finished, "Tie"
        else:
            return finished, coordinates
    else:
        if coordinates is None:
            return finished, "In process"
        else:
            return finished, coordinates


def copy_board(triqui):
    new_triqui = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(3):
        for j in range(3):
            new_triqui[i][j] = triqui[i][j]
    return new_triqui


def draw_move(player, triqui, x, y):
    new_board = copy_board(triqui)
    new_board[x][y] = player
    return new_board


def find_branches(triqui, player):
    boards = []
    for x in range(3):
        for y in range(3):
            if triqui[x][y] == " ":
                new_board = draw_move(player, triqui, x, y)
                boards.append(new_board)

    return boards


def best_move(triqui, player):
    best_score = -infinity
    boards = find_branches(triqui, player)

    for board in boards:
        # print_board(board)
        score = (mini_max(board, "o"))
        # print(score)

        if score > best_score:
            best_score = score
            my_best_move = board

    return my_best_move


def mini_max(triqui, player):
    # Check winner
    finished, winner = check_winner(triqui)

    if winner == "x":
        # print("x")
        return 1
    if winner == "o":
        # print("o")
        return -1
    if winner == "Tie":
        # print("tie")
        return 0

    if player == "x":
        boards = find_branches(triqui, "x")
        results = []
        for board in boards:
            # print_board(board)
            result = mini_max(board, "o")
            results.append(result)

    if player == "o":
        boards = find_branches(triqui, "o")
        results = []
        for board in boards:
            # print_board(board)
            result = mini_max(board, "x")
            results.append(result)

    # Store the variables of each level to later compare them
    globalresults = results

    # Decide best move depending on whether the player is maximizing or minimizing
    if player == "x":
        best_score = max(globalresults)
        return best_score

    if player == "o":
        best_score = min(globalresults)
        return best_score


def start():
    initial_dialogue = input(
        "Welcome to an exciting game of tic tac toe. Are you ready to challenge an unbeatable computer? (yes/no)")
    if initial_dialogue == "yes":
        initial_player = input(
            "Terrific. For this round, you will play with the o. Do you want the computer to start? (yes/no)")
        if initial_player == "yes":
            play('x', triqui)
        elif initial_player == "no":
            play('o', triqui)
        else:
            print("Please insert a valid answer")
            start()
    elif initial_dialogue == "no":
        return
    else:
        print("Please insert a valid answer")
        start()


def play(player, triqui):
    finished, winner = check_winner(triqui)
    if finished and winner == 'o':
        print("Congratulations. You have won")
        return
    elif finished and winner == 'x':
        print("Ups. It seems like the computer has won. Who would have seen this coming?")
        return
    elif finished and winner == "tie":
        print("Well played. It is a tie")
        return
    else:
        if player == 'o':
            block_num = input("It is your turn. Please write as a pair of coordinates separated by a coma where you "
                              "want to play (for instance, 1,2 or 0,0)")
            f_coordinate = int(block_num[0])
            s_coordinate = int(block_num[2])
            if triqui[f_coordinate][s_coordinate] is ' ':
                new_board = draw_move('o', triqui, f_coordinate, s_coordinate)
                print_board(new_board)
                print("Now it is the turn of the computer")
                play('x', new_board)
            else:
                print("Block is not empty, ya blockhead! Choose again: ")
                play('o', triqui)

        if player == 'x':
            new_board = best_move(triqui, 'x')
            print_board(new_board)
            play('o', new_board)


start()