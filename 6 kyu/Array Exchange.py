def get_grade(s1, s2, s3):
    # Code here
    total = s1+s2+s3
    final = total/3
    note = 0
    if final >= 90:
        note = 'A'
    elif final < 90 and final >= 80:
        note = 'B'
    elif final < 80 and final >= 70:
        note = 'C'
    elif final < 70 and final >= 60:
        note = 'D'
    elif final < 60:
        note = 'F'
    return note


# mean = sum([s1,s2,s3])/3
