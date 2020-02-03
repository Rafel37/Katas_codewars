def count_sheep(n):
    for i in range(n):
        if i == 0:
            solution = str(i + 1) + " sheep..."
        else:
            solution += str(i + 1) + " sheep..."
    return solution