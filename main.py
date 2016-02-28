import json
import sys
from libs.game import Game
from libs.animate_game import animate

with open(sys.argv[1]) as json_file:
    config = json.load(json_file)

game = Game(config)
animate(game)
