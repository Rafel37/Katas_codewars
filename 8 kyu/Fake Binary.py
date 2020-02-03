def fake_bin(x):
    x_list = list(x)
    int_list = list(map(lambda x: int(x), x_list))
    list_result = []
    for item in int_list:
        if item >= 5:
            list_result.append("1")
        else: list_result.append("0")
    return "".join(list_result)