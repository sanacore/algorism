def exe(lost):
    #lost = input()
    #lost = int(lost)

    #print('lost: ', lost)

    left = 52 - lost

    #print('left: ', left)


    max = int(left/5)

    if max > 8:
        max = 8

    if lost > 25:
        min = 0

    if lost >= 24 and lost <= 25:
        min = 1
    if lost >= 22 and lost <= 23:
        min = 2
    if lost >= 20 and lost <= 21:
        min = 3
    if lost >= 18 and lost <= 19:
        min = 4
    if lost >= 16 and lost <= 17:
        min = 5
    if lost >= 12 and lost <= 15:
        min = 6
    if lost >= 6 and lost <= 11:
        min = 7
    if lost < 6:
        min = 8

    print(left, min, max)


if __name__ == "__main__":
    # execute only if run as a script

    for i in range(0, 53):
        exe(i)