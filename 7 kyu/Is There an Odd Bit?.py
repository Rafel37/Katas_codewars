def any_odd(x):
    # Write code here...
    binary = bin(x).replace('0b', '')
    if len(binary) < 32:
        binary = binary.zfill(32)
    bit = binary[0::2]

    if all(i == 0 for i in map(int, str(bit))):
        return 0
    else:
        return 1
