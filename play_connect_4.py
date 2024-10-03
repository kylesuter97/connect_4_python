
import grid
import cells
import colorama 
colorama.init(convert=True)

# gameboard creation

print(grid.print_grid())
active_player = "p1"
cells.cell_A1.enter(active_player)
print(grid.print_grid())



