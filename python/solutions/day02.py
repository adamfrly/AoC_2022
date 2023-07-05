import time
from python.utils import get_input

day = 2
RESULTS = {"Z": "B", "X": "C", "Y": "A"}

def main(input):
    points = 0
    games = [game.split(" ") for game in input.split("\n")]
    for game in games:
        game_points = ord(game[1]) - 87
        if ord(game[0]) + 23 == ord(game[1]):
            game_points += 3
        elif RESULTS[game[1]] == game[0]:
            game_points += 6
        print(game_points)
        points += game_points
    print(points)


if __name__ == "__main__":
    start = time.perf_counter()
    main(get_input(day))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")