import tic_tac_toe_func as my_game


def game_on():
    game_status = True
    while game_status:
        keep_playing = input("Do You Want To Continue Playing?\nEnter 'Yes'/'Y' or 'No' /'N'==>\n")
        if keep_playing == 'No' or keep_playing.capitalize() == 'No' or keep_playing.upper() == 'N':
            print("YOU HAVE EXIT THE GAME")
            game_status = False
        elif keep_playing == 'Yes' or keep_playing.capitalize() == 'Yes' or keep_playing.upper() == 'Y':
            players = my_game.select_player()
            game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            my_game.display_board(game_board)
            turn = 0
            while True:
                change = my_game.player_input(players, turn, game_status)
                game_board = my_game.change_board(change, game_board, players, turn)
                my_game.display_board(game_board)
                turn += 1
                conclusion = my_game.game_end(game_board, players)
                if conclusion:
                    break
        else:
            print(f"Answer Not Understood")


default_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("POSITIONS ON THE BOARD ARE AS FOLLOWS\n")
my_game.display_board(default_board)
game_on()
