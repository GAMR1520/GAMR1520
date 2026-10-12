import tkinter as tk
from random import randint, choice

import core

normal = ("Helvetica", 24, "bold")

bg1 = "#faf8ef"
bg2 = "#bbada0"
fg1 = "#776e65"

tile_colours = {
    2: "#eee4da",
    4: "#eee1c9",
    8: "#f3b27a",
    16: "#f69664",
    32: "#f77c5f",
    64: "#f75f3b",
    128: "#edd073",
    256: "#edcc62",
    512: "#edc950",
    1024: "#edc53f",
    2048: "#edc22e"
}
font_colours = {
    2: "#776e65",
    4: "#776e65"
}
fonts = {
    128: ("Helvetica", 20, "bold"),
    256: ("Helvetica", 20, "bold"),
    512: ("Helvetica", 20, "bold"),
    1024: ("Helvetica", 16, "bold"),
    2048: ("Helvetica", 16, "bold")
}

class Tile(tk.Label):
    """
    A custom label whose colours and font are determined by the value it's given
    """
    def __init__(self, parent):
        super().__init__(parent, anchor=tk.CENTER)

    def set(self, value):
        self.configure(
            text=value or " ",
            bg=tile_colours.get(value, "#cdc1b4"),
            fg=font_colours.get(value, "#f9f6f2"),
            font=fonts.get(value, normal)
        )


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("py2048")
        self.configure(padx=50, pady=50, bg=bg1)
        self.columnconfigure(1, weight=1)

        self.score = tk.IntVar()
        tk.Label(text="SCORE: ", font=normal, bg=bg1, fg=fg1).grid(column=0, row=0)
        tk.Label(textvariable=self.score, font=normal, bg=bg1, fg=fg1).grid(column=1, row=0, sticky="w")

        frame = tk.Frame(padx=10, pady=10, bg=bg2)
        frame.grid(column=0, row=1, columnspan=2, sticky="news")

        self.tiles = {}
        for row in range(4):
            for col in range(4):
                self.tiles[(row, col)] = Tile(frame)
                self.tiles[(row, col)].grid(row=row, column=col, sticky="news", padx=10, pady=10)

        cell_size = 150
        for i in range(4):
            frame.rowconfigure(i, minsize=cell_size)
            frame.columnconfigure(i, minsize=cell_size)

        self.game_over_message = tk.Label(text="GAME OVER\n'r' to restart", font=normal, bg="white", padx=20, pady=20)
        self.game_over_message.grid(row=1, column=0, columnspan=2)
        # self.game_over_message.grid_remove()

        self.moves = {
            "Left": core.move_left,
            "Right": core.move_right,
            "Up": core.move_up,
            "Down": core.move_down,
        }
        for key in self.moves:
            self.bind(f"<{key}>", self.move_handler)

        self.bind(f"<KeyPress-r>", lambda ev: self.restart())

        self.point_functions = {
            "Left": core.horizontal_points,
            "Right": core.horizontal_points,
            "Up": core.vertical_points,
            "Down": core.vertical_points,
        }

        self.restart()
        self.update()


    def restart(self):
        self.grid = [[None, None, None, None],
                     [None, None, None, None],
                     [None, None, None, None],
                     [None, None, None, None]]

        self.set_random_empty_tile(2)
        self.set_random_empty_tile(2)
        self.score.set(0)
        self.game_over = False
        self.update()

    def move_handler(self, ev):
        self.process_command(ev.keysym)
        self.update()

    def update(self):
        for row in range(4):
            for col in range(4):
                self.tiles[(row, col)].set(self.grid[row][col] or "")
        if self.game_over:
            self.game_over_message.grid()
        else:
            self.game_over_message.grid_remove()


    def set_random_empty_tile(self, value):
        while(True):
            row = randint(0, 3)
            col = randint(0, 3)
            if not self.grid[row][col]:
                break
        self.grid[row][col] = value


    def process_command(self, command):
        next_grid = self.moves[command](self.grid)
        if next_grid != self.grid:
            self.score.set(self.score.get() + self.point_functions[command](self.grid))
            self.grid = next_grid
            new_tile = choice([2, 2, 2, 4])
            self.set_random_empty_tile(new_tile)
            self.game_over = core.is_game_over(self.grid)



if __name__ == "__main__":
    g = Game()
    g.mainloop()