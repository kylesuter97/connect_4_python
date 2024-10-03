
import game_flow
import grid
import cells
import check_moves
import colorama 
colorama.init(convert=True)


def play_game():
    print(game_flow.welcome_statement)
    print(grid.print_grid())
    game_flow.play()

    
play_game()




