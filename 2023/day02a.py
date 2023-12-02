# games = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
def validate(games: str) -> bool:
    valid_cubes = {"red": 12, "green": 13, "blue": 14}

    for game in games.split("; "):
        for cubes in game.split(", "):
            amount, color = cubes.split(" ")
            if int(amount) > valid_cubes[color]:
                return False

    return True


total = 0

for line in open(0):
    game_id, games = line.strip("\n").replace("Game ", "").split(": ")

    if validate(games):
        total += int(game_id)

print(total)
