import pandas as pd

class Map:
    def __init__(self):
        self.cells = []
        self.entrance = []
        self.exit = []
        with open('src/map.txt', 'r') as map_file:
            line = map_file.readline()
            row = 0
            while line:
                col = 0
                col_cells = []
                for c in line:
                    if c != '\n':
                        col_cells.append(c)
                    if c == 'B':
                        self.entrance.append(row)
                        self.entrance.append(col)
                    if c == 'E':
                        self.exit.append(row)
                        self.exit.append(col)
                    col += 1
                row += 1
                self.cells.append(col_cells)
                line = map_file.readline()

        self.num_cols = len(self.cells)
        self.num_rows = len(self.cells[0])
    
    def show_map(self):
        ascii_dec = 97 # start with lowercase a
        columns = []
        rows = []
        for i in range(self.num_cols):
            columns.append(chr(ascii_dec))
            ascii_dec += 1
        for i in range(self.num_rows):
            rows.append(i + 1)
        df = pd.DataFrame(self.cells, columns, rows)
        print(df)