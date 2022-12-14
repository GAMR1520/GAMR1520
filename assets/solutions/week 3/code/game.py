from random import randint, choice

import core

class Game:
    def __init__(self):
        self.grid = [[None, None, None, None],
                     [None, None, None, None],
                     [None, None, None, None],
                     [None, None, None, None]]

        self.set_random_empty_tile(2)
        self.set_random_empty_tile(2)

        self.moves = {
            "W": core.move_up,
            "A": core.move_left,
            "S": core.move_down,
            "D": core.move_right
        }
        self.point_functions = {
            "W": core.vertical_points,
            "A": core.horizontal_points,
            "S": core.vertical_points,
            "D": core.horizontal_points            
        }
        self.score = 0

    def __str__(self):
        tiles = [[str(t or ".").center(4) for t in row] for row in self.grid]
        result = "\n".join([" ".join(row) for row in tiles])
        msg = ""
        if not self.playing:
            msg = "\nYOU QUIT THE GAME\n"
        if self.game_over:
            msg = "\nGAME OVER\n"
        return f"\nSCORE: {self.score}\n\n{result}\n{msg}"

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
            self.score += self.point_functions[command](self.grid)
            self.grid = next_grid
            new_tile = choice([2, 2, 2, 4])
            self.set_random_empty_tile(new_tile)
            self.game_over = core.is_game_over(self.grid)

    def next_move(self):
        print(self)
        commands = input("\nmove (W=Up, A=Left, S=Down, D=Right, Q=Quit): ").upper()
        for c in commands:
            try:
                self.process_command(c)
            except KeyError:
                if c == "Q":
                    self.playing = False
                else:
                    print(f"\nInvalid command: {c}")

    def play(self):
        self.game_over = False
        self.playing = True
        while self.playing and not self.game_over:
            self.next_move()
        print(self)

if __name__ == "__main__":
    g = Game()
    g.play()