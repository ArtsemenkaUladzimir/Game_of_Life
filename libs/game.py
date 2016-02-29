from libs.config_parser import ConfigParser


class Game:
    def __init__(self, config):
        self.config = ConfigParser(config)
        self.generation = self.config.first_generation

    def next_generation(self):

        next_gen = [[0] * self.config.width for i in range(self.config.height)]

        for x, row in enumerate(self.generation):
            for y, cell in enumerate(row):
                neighbours = self.__neighbours(x, y)
                if neighbours == 3 or (neighbours == 2 and cell):
                    next_gen[x][y] = 1

        self.generation = next_gen
        return next_gen

    def get_active(self):
        active_cells = [[], []]

        for x, row in enumerate(self.generation):
            for y, cell in enumerate(row):
                if cell:
                    active_cells[0].append(y)
                    active_cells[1].append(x)

        return active_cells

    def __neighbours(self, row, col):
        count = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if not x == y == 0 \
                        and self.generation[(row + x) % self.config.height][(col + y) % self.config.width]:
                    count += 1
        return count
