import random
import time


class GameOfLife:
    grid = []
    width = 5
    heigth = 5

    def __init__(self):
        self.width = int(input("Width: "))
        self.heigth = int(input("Heigth: "))
        self.grid = [
            ["😀" if random.randint(0, 1) else "💀" for column in range(self.width)]
            for row in range(self.heigth)
        ]
        self.print()

    def print(self):
        for row in self.grid:
            print(
                str(row)
                .replace("'", "")
                .replace(", ", "")
                .replace("[", "")
                .replace("]", "")
            )
        print("\n")

    def is_alive(self, x: int, y: int) -> int:
        if x < 0 or y < 0 or x >= self.heigth or y >= self.width:
            return 0
        if self.grid[x][y] == "😀":
            return 1
        return 0

    def neighbor_count(self, x: int, y: int) -> int:
        living_neighbors = 0
        for row_offset in range(-1, 2):
            if row_offset != 0:
                for column_offset in range(-1, 2):
                    living_neighbors += self.is_alive(x + row_offset, y + column_offset)
            else:
                for column_offset in range(-1, 2, 2):
                    living_neighbors += self.is_alive(x + row_offset, y + column_offset)
        return living_neighbors

    def logic(self):
        newgrid = [["💀" for column in range(self.width)] for row in range(self.heigth)]
        for x in range(self.heigth):
            for y in range(self.width):
                living_neighbors = self.neighbor_count(x, y)
                if self.is_alive(x, y) == 1:
                    if living_neighbors == 3 or living_neighbors == 2:
                        newgrid[x][y] = "😀"
                else:
                    if living_neighbors == 3:
                        newgrid[x][y] = "😀"

        self.grid = newgrid
        self.print()


game = GameOfLife()
while True:
    time.sleep(0.5)
    game.logic()
