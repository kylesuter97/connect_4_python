
import cells
import grid

# entry is user input of cell position
def check_vertical(entry):
    if entry == "":
        return False
    reference_cell = cells.cell_dict[entry]
    cell_entry = reference_cell.player_in
    column_list = cells.cell_list[reference_cell.list_index]
    
    if cell_entry is not None:
        for i in range(3):  # Only need to check indices 0 to 2
            if (column_list[i].player_in == cell_entry and column_list[i + 1].player_in == cell_entry
            and column_list[i + 2].player_in == cell_entry and column_list[i + 3].player_in == cell_entry):
                return True
            
    return False
    
def winner_check(entry):
    if check_vertical(entry) is True:
        return True
    else:
        return False




