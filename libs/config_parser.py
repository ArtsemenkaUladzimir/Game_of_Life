class ConfigParser:
    def __init__(self, config):
        self.width = config.get("width") or 50
        self.height = config.get("height") or 50

        start_x = config.get("x") or 0
        start_y = config.get("y") or 0
        active_cell = []

        for x, row in enumerate(config["firstGeneration"]):
            for y, cell in enumerate(row):
                if cell == 1:
                    active_cell.append([x + start_x, y + start_y])

        self.first_generation = [[0] * self.width for i in range(self.height)]

        for cell in active_cell:
            self.first_generation[cell[0]][cell[1]] = 1
