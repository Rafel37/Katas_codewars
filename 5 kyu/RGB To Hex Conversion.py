def rgb(r, g, b):
    #your code here :)
    hexa = ''
    for item in [r,g,b]:
        if item < 0:
            item = 0
        elif item > 255:
            item = 255
        hexa += str(hex(item)).replace('0x','').upper().zfill(2)
    return hexa