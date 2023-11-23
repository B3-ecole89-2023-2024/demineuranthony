import time
import Display
import Game


def game(width, height, bombs, displayed_map, mine_map):
    start_time = time.time()
    win = False
    lose = False
    while not win and not lose:
        if displayed_map.count("█") == bombs:
            print("win")
            win = True
            time.sleep(5)

        elif len(displayed_map) == 1:
            print("lose")
            Display.displayMap(width, mine_map)
            lose = True
            time.sleep(5)
        else:
            Display.displayMap(width, displayed_map)
            print(f"\nBombes restantes : {bombs - displayed_map.count('⚑')}")
            print(f"Temps : {(time.time() - start_time):.2f} secondes")
            displayed_map = Game.selection(
                width, height, displayed_map, mine_map)
