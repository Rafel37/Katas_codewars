def duplicate_count(text):
    # Your code goes here
    acc = 0
    lista = [n.lower() for n in text]
    new_set = set(lista)
    print(new_set)
    for i in new_set:
        number = lista.count(i)
        if number > 1:
            acc += 1
    return acc