
import colorama 
colorama.init(convert=True)

# class to create each cell of the gameboard, which can be filled or unfilled
class Cell:
    def __init__(self, column, row):
        self.is_empty = True
        self.contains = "   "
        self.column = column
        self.list_index = {chr(i): i - 65 for i in range(65, 72)}.get(self.column, None)
        self.row = row
        self.player_in = None
        self.name = column + str(row)
    
    def __repr__(self) -> str:
        return self.contains

    def enter(self, active_player):
        if self.is_empty is True:
            # checks if rows below cell are populated to be able to enter into higher cell
            if self.row > 1:
                # searches for below cell variable in cell list
                if cell_list[self.list_index][cell_list[self.list_index].index(self) - 1].is_empty is not True:
                    if active_player == "p1":
                        self.contains = colorama.Back.RED + "   " + colorama.Back.BLACK
                        self.player_in = "p1"
                        self.is_empty = False
                    elif active_player == "p2":
                        self.contains = colorama.Back.YELLOW + "   " + colorama.Back.BLACK
                        self.player_in = "p2"
                        self.is_empty = False
                else:
                    print("You can't do that! No Wingardium Leviosa allowed!")
            else:
                if active_player == "p1":
                    self.contains = colorama.Back.RED + "   " + colorama.Back.BLACK
                    self.player_in = "p1"
                    self.is_empty = False
                elif active_player == "p2":
                    self.contains = colorama.Back.YELLOW + "   " + colorama.Back.BLACK
                    self.player_in = "p2"
                    self.is_empty = False

# create instances of Cell class 
cell_A1, cell_A2, cell_A3, cell_A4, cell_A5, cell_A6 = Cell("A", 1), Cell("A", 2), Cell("A", 3), Cell("A", 4), Cell("A", 5), Cell("A", 6)
cell_B1, cell_B2, cell_B3, cell_B4, cell_B5, cell_B6 = Cell("B", 1), Cell("B", 2), Cell("B", 3), Cell("B", 4), Cell("B", 5), Cell("B", 6)
cell_C1, cell_C2, cell_C3, cell_C4, cell_C5, cell_C6 = Cell("C", 1), Cell("C", 2), Cell("C", 3), Cell("C", 4), Cell("C", 5), Cell("C", 6)
cell_D1, cell_D2, cell_D3, cell_D4, cell_D5, cell_D6 = Cell("D", 1), Cell("D", 2), Cell("D", 3), Cell("D", 4), Cell("D", 5), Cell("D", 6)
cell_E1, cell_E2, cell_E3, cell_E4, cell_E5, cell_E6 = Cell("E", 1), Cell("E", 2), Cell("E", 3), Cell("E", 4), Cell("E", 5), Cell("E", 6)
cell_F1, cell_F2, cell_F3, cell_F4, cell_F5, cell_F6 = Cell("F", 1), Cell("F", 2), Cell("F", 3), Cell("F", 4), Cell("F", 5), Cell("F", 6)
cell_G1, cell_G2, cell_G3, cell_G4, cell_G5, cell_G6 = Cell("G", 1), Cell("G", 2), Cell("G", 3), Cell("G", 4), Cell("G", 5), Cell("G", 6)

# used for positional checks
cell_list = [[cell_A1, cell_A2, cell_A3, cell_A4, cell_A5, cell_A6],
             [cell_B1, cell_B2, cell_B3, cell_B4, cell_B5, cell_B6],
             [cell_C1, cell_C2, cell_C3, cell_C4, cell_C5, cell_C6],
             [cell_D1, cell_D2, cell_D3, cell_D4, cell_D5, cell_D6],
             [cell_E1, cell_E2, cell_E3, cell_E4, cell_E5, cell_E6],
             [cell_F1, cell_F2, cell_F3, cell_F4, cell_F5, cell_F6],
             [cell_G1, cell_G2, cell_G3, cell_G4, cell_G5, cell_G6]
             ]

# used for locating correct variable based on user input
cell_dict = {
    "A1": cell_A1, "A2": cell_A2, "A3": cell_A3, "A4": cell_A4, "A5": cell_A5, "A6": cell_A6,
    "B1": cell_B1, "B2": cell_B2, "B3": cell_B3, "B4": cell_B4, "B5": cell_B5, "B6": cell_B6,
    "C1": cell_C1, "C2": cell_C2, "C3": cell_C3, "C4": cell_C4, "C5": cell_C5, "C6": cell_C6,
    "D1": cell_D1, "D2": cell_D2, "D3": cell_D3, "D4": cell_D4, "D5": cell_D5, "D6": cell_D6,
    "E1": cell_E1, "E2": cell_E2, "E3": cell_E3, "E4": cell_E4, "E5": cell_E5, "E6": cell_E6,
    "F1": cell_F1, "F2": cell_F2, "F3": cell_F3, "F4": cell_F4, "F5": cell_F5, "F6": cell_F6,
    "G1": cell_G1, "G2": cell_G2, "G3": cell_G3, "G4": cell_G4, "G5": cell_G5, "G6": cell_G6
    }




