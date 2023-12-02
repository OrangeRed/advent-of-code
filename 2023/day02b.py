import math


# games = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
def find_min_cubes(games: str) -> dict[str, int]:
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    for game in games.split("; "):
        for cubes in game.split(", "):
            amount, color = cubes.split(" ")
            if int(amount) > min_cubes[color]:
                min_cubes[color] = int(amount)

    return min_cubes


total = 0

for line in open(0):
    game_id, games = line.strip("\n").replace("Game ", "").split(": ")

    min_cubes = find_min_cubes(games)

    total += math.prod(min_cubes.values())

print(total)
