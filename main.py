
import sys
sys.path.append("./scripts")

from scripts.game import Game

g = Game()


while g.running:

    g.playing = True
    g.game_loop()
