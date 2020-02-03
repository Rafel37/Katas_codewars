
def points(games):
    result = 0
    for game in games:
        local_points = game[0]
        visitor_points = game[2]
        if local_points > visitor_points:
           result += 3
        elif local_points < visitor_points:
           result += 0
        else:
           result += 1
    return result