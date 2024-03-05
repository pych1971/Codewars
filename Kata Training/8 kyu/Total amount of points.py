def points(games):
    sum = 0
    for game in games:
        result = int(game.split(':')[0]) - int(game.split(':')[1])
        if result > 0:
            sum += 3
        elif result == 0:
            sum += 1
    return sum
