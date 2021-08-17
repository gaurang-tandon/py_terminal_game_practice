# FUNCTION TO DISPLAY THE BOARD
def display_board(board):
    print(f'''
CURRENT BOARD ====>

    {board[1]} | {board[2]} | {board[3]}
    --|---|--
    {board[4]} | {board[5]} | {board[6]}
    --|---|--
    {board[7]} | {board[8]} | {board[9]}
    ''')


# ------------------------------------------------------------------------------------------------------- #


# FUNCTION TO SELECT PLAYER
def select_player():
    player_option = ['X', 'O']
    player_1 = input("Player 1 is 'X' or 'O' ? => ")
    player_option.remove(player_1)
    player_2 = player_option[0]
    print(f"""
    Player 1 is {player_1}
    Player 2 in {player_2}
    """)
    players = ['#', player_1, player_2]
    return players


# ------------------------------------------------------------------------------------------------------- #


# FUNCTION TO TAKE PLAYER INPUT
def player_input(players, turn, game_stat):
    while game_stat:
        player_turn = turn % 2
        if player_turn == 0:
            print(f'Player 1 - {players[1]}\'s turn')
            position_to_change = int(input(f"ENTER POSITION TO PLACE '{players[1]}'==> "))
        else:
            print(f'Player 2 - {players[2]}\'s turn')
            position_to_change = int(input(f"ENTER POSITION TO PLACE '{players[2]}'==> "))

        return [position_to_change, player_turn]


# ------------------------------------------------------------------------------------------------------- #


# FUNCTION TO CHANGE BOARD VALUE

def change_board(change_details, game_board, players, turn):
    if change_details[1] == 0:
        if game_board[(change_details[0])] == " ":
            game_board[(change_details[0])] = players[1]
        else:
            print(f"Position Not Empty")
            change_details = player_input(players, turn)
            change_board(change_details, game_board, players, turn)
    else:
        if game_board[(change_details[0])] == " ":
            game_board[(change_details[0])] = players[2]
        else:
            print(f"Position Not Empty")
            change_details = player_input(players, turn)
            change_board(change_details, game_board, players, turn)
    return game_board


# ------------------------------------------------------------------------------------------------------- #


# WIN CASE OR STALEMATE FUNCTION
def game_end(g_b, pl):
    if (g_b[1] == g_b[5] == g_b[9] == pl[1] or g_b[7] == g_b[5] == g_b[3] == pl[1] or g_b[1] == g_b[2] == g_b[3] == pl[
        1] or
            g_b[4] == g_b[5] == g_b[6] == pl[1] or g_b[7] == g_b[8] == g_b[9] == pl[1] or g_b[1] == g_b[4] == g_b[7] ==
            pl[1] or
            g_b[2] == g_b[5] == g_b[8] == pl[1] or g_b[3] == g_b[6] == g_b[9] == pl[1]):
        print(f"""
                ************************
                ***PLAYER 1 '{pl[1]}' WINS****
                ********GAME END********
                ************************
        """)
        return True
    elif (g_b[1] == g_b[5] == g_b[9] == pl[2] or g_b[7] == g_b[5] == g_b[3] == pl[2] or g_b[1] == g_b[2] == g_b[3] ==
          pl[2] or
          g_b[4] == g_b[5] == g_b[6] == pl[2] or g_b[7] == g_b[8] == g_b[9] == pl[2] or g_b[1] == g_b[4] == g_b[7] ==
          pl[2] or
          g_b[2] == g_b[5] == g_b[8] == pl[2] or g_b[3] == g_b[6] == g_b[9] == pl[2]):
        print(f"""
                ************************
                ***PLAYER 2 '{pl[2]}' WINS****
                ********GAME END********
                ************************
        """)
        return True
    elif " " not in g_b:
        print(f"""
                ************************
                *******STALEMATE********
                ********GAME END********
                ************************
        """)
        return True
    else:
        pass

# ------------------------------------------------------------------------------------------------------- #

