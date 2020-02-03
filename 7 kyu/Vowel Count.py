def getCount(string):
    vocal=['a','e','i','o','u']
    cont = 0
    for letter in string:
        if letter in vocal:
            print(letter)
            cont += 1
    return cont