
import colorama 
colorama.init(convert=True)

# class to create each cell of the gameboard, which can be filled or unfilled
class Cell:
    def __init__(self, column, row):
        self.is_empty = True
        self.contains = "   "
        self.player_in = None
    
    def __repr__(self) -> str:
        return self.contains

    def enter(self, active_player):
        if self.is_empty is True:
            if active_player == "p1":
                self.contains = colorama.Back.RED + "   " + colorama.Back.BLACK
                self.player_in = "p1"
            elif active_player == "p2":
                self.contains = colorama.Back.YELLOW + "   " + colorama.Back.BLACK
                self.player_in = "p2"

cell_A1, cell_A2, cell_A3, cell_A4, cell_A5, cell_A6 = Cell("A", 1), Cell("A", 2), Cell("A", 3), Cell("A", 4), Cell("A", 5), Cell("A", 6)
cell_B1, cell_B2, cell_B3, cell_B4, cell_B5, cell_B6 = Cell("B", 1), Cell("B", 2), Cell("B", 3), Cell("B", 4), Cell("B", 5), Cell("B", 6)
cell_C1, cell_C2, cell_C3, cell_C4, cell_C5, cell_C6 = Cell("C", 1), Cell("C", 2), Cell("C", 3), Cell("C", 4), Cell("C", 5), Cell("C", 6)
cell_D1, cell_D2, cell_D3, cell_D4, cell_D5, cell_D6 = Cell("D", 1), Cell("D", 2), Cell("D", 3), Cell("D", 4), Cell("D", 5), Cell("D", 6)
cell_E1, cell_E2, cell_E3, cell_E4, cell_E5, cell_E6 = Cell("E", 1), Cell("E", 2), Cell("E", 3), Cell("E", 4), Cell("E", 5), Cell("E", 6)
cell_F1, cell_F2, cell_F3, cell_F4, cell_F5, cell_F6 = Cell("F", 1), Cell("F", 2), Cell("F", 3), Cell("F", 4), Cell("F", 5), Cell("F", 6)
cell_G1, cell_G2, cell_G3, cell_G4, cell_G5, cell_G6 = Cell("G", 1), Cell("G", 2), Cell("G", 3), Cell("G", 4), Cell("G", 5), Cell("G", 6)

cell_list = [cell_A1, cell_A2, cell_A3, cell_A4, cell_A5, cell_A6,
             cell_B1, cell_B2, cell_B3, cell_B4, cell_B5, cell_B6,
             cell_C1, cell_C2, cell_C3, cell_C4, cell_C5, cell_C6,
             cell_D1, cell_D2, cell_D3, cell_D4, cell_D5, cell_D6,
             cell_E1, cell_E2, cell_E3, cell_E4, cell_E5, cell_E6,
             cell_F1, cell_F2, cell_F3, cell_F4, cell_F5, cell_F6,
             cell_G1, cell_G2, cell_G3, cell_G4, cell_G5, cell_G6]



