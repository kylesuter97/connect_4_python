
import grid
import cells
import check_moves

welcome_statement = """
Welcome to Connect 4!
        
Player 1 will go first, and their entries will be in Red. Player 2's will be in Yellow.
Please make your entries by typing in the cell position that you would like to enter, 
e.g. "A1", or "C6".

The game will be finished when one player enters 4 cells that are directly connected together,
this can be vertically, horizontally, or diagonally. 

Good Luck!
"""

def play():
    active_player = "p1"
    player_entry = ""
    while (grid.grid_full() is False) and (check_moves.winner_check(player_entry) is False):
        player_entry = input(f"Player {active_player[1]}, please type a cell to populate: ").upper()
        if player_entry in cells.cell_dict.keys():
            cells.cell_dict[player_entry].enter(active_player)
            # check if cell just entered is still empty, if so it was an invalid entry as it was floating
            if cells.cell_dict[player_entry].is_empty is True:
                continue
            else:   
                print(grid.print_grid())
                if active_player == "p1":
                    active_player = "p2"
                elif active_player == "p2":
                    active_player = "p1"
        else:
            print("Not a valid entry! Please try again.")
            continue
    print("Game over!")
    if check_moves.winner_check(player_entry) is True:
        print(f"Player {cells.cell_dict[player_entry].player_in[1]} wins!")
    elif grid.grid_full() is True:
        print("No one won! There are no spaces left on the board.")

        



