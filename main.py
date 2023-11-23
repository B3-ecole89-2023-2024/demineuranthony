import Play
import Display
import Game


def main():
    Display.menu()

    x, y, b = Display.selecteddifficulty()

    tab = list(x * y * "■")

    Play.game(x, y, b, tab, Game.init_mine(x, y, b))


main()
