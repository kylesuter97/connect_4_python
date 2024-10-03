
import cells
import grid

# entry is user input of cell position
def check_vertical(entry):
    if entry == "" or entry not in cells.cell_dict.keys() or cells.cell_dict[entry].player_in is None:
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

def check_horizontal(entry):
    if entry == "" or entry not in cells.cell_dict.keys() or cells.cell_dict[entry].player_in is None:
        return False
    reference_cell = cells.cell_dict[entry]
    row_index = reference_cell.row - 1
    cell_entry = reference_cell.player_in
    row_list = []
    for i in cells.cell_list:
        row_list.append(i[row_index])

    if cell_entry is not None:
        for i in range(4):  # Only need to check indices 0 to 3
            if (row_list[i].player_in == cell_entry and row_list[i + 1].player_in == cell_entry
            and row_list[i + 2].player_in == cell_entry and row_list[i + 3].player_in == cell_entry):
                return True
    return False


def check_diagonal(entry):
    if entry == "" or entry not in cells.cell_dict.keys() or cells.cell_dict[entry].player_in is None:
        return False
    reference_cell = cells.cell_dict[entry]
    cell_entry = reference_cell.player_in
    grid = cells.cell_list
    rows = 6 
    cols = 7
    # Check down-right diagonals
    for row in range(rows - 3):  # Stop at row 2 to avoid out-of-bounds
        for col in range(cols - 3):  # Stop at col 3 to avoid out-of-bounds
            if grid[row][col].player_in == cell_entry and \
               grid[row + 1][col + 1].player_in == cell_entry and \
               grid[row + 2][col + 2].player_in == cell_entry and \
               grid[row + 3][col + 3].player_in == cell_entry:
                return True
    # Check up-right diagonals
    for row in range(3, rows):  # Start from row 3 (bottom) to avoid out-of-bounds
        for col in range(cols - 3):  # Stop at col 3 to avoid out-of-bounds
            if grid[row][col].player_in == cell_entry and \
               grid[row - 1][col + 1].player_in == cell_entry and \
               grid[row - 2][col + 2].player_in == cell_entry and \
               grid[row - 3][col + 3].player_in == cell_entry:
                return True

    return False
    
    
def winner_check(entry):
    if check_vertical(entry) is True:
        return True
    elif check_horizontal(entry) is True:
        return True
    elif check_diagonal(entry) is True:
        return True
    else:
        return False




