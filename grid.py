
import cells

# gameboard creation
def print_grid():
    return f"""
           A     B     C     D     E     F     G
        +-----+-----+-----+-----+-----+-----+-----+
      6 + {cells.cell_A6} + {cells.cell_B6} + {cells.cell_C6} + {cells.cell_D6} + {cells.cell_E6} + {cells.cell_F6} + {cells.cell_G6} + 6
        +-----+-----+-----+-----+-----+-----+-----+
      5 + {cells.cell_A5} + {cells.cell_B5} + {cells.cell_C5} + {cells.cell_D5} + {cells.cell_E5} + {cells.cell_F5} + {cells.cell_G5} + 5
        +-----+-----+-----+-----+-----+-----+-----+
      4 + {cells.cell_A4} + {cells.cell_B4} + {cells.cell_C4} + {cells.cell_D4} + {cells.cell_E4} + {cells.cell_F4} + {cells.cell_G4} + 4
        +-----+-----+-----+-----+-----+-----+-----+
      3 + {cells.cell_A3} + {cells.cell_B3} + {cells.cell_C3} + {cells.cell_D3} + {cells.cell_E3} + {cells.cell_F3} + {cells.cell_G3} + 3
        +-----+-----+-----+-----+-----+-----+-----+
      2 + {cells.cell_A2} + {cells.cell_B2} + {cells.cell_C2} + {cells.cell_D2} + {cells.cell_E2} + {cells.cell_F2} + {cells.cell_G2} + 2
        +-----+-----+-----+-----+-----+-----+-----+
      1 + {cells.cell_A1} + {cells.cell_B1} + {cells.cell_C1} + {cells.cell_D1} + {cells.cell_E1} + {cells.cell_F1} + {cells.cell_G1} + 1
        +-----+-----+-----+-----+-----+-----+-----+
           A     B     C     D     E     F     G    
        """

def grid_full():
    count_empty = 0
    for l in cells.cell_list:
        for c in l:
            if c.is_empty is True:
                count_empty += 1
            else:
                continue
    if count_empty != 0:
        return False
    else:
        return True

    