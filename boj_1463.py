import sys

D = [0]*10000001

var = int(sys.stdin.readline())

D[0] = 0
D[1] = 0
D[2] = 1
D[3] = 1

candidates = [0]*3

candidates[0] = 1000000
candidates[1] = 1000000
candidates[2] = 1000000

for idx in range(4, var+1):

    if idx % 3 == 0:
        candidates[2] = (D[int(idx / 3)]+1)
    if idx % 2 == 0:
        candidates[1] = (D[int(idx / 2)] + 1)
    if idx % 1 == 0:
        candidates[0] = (D[idx - 1] + 1)

    D[idx] = min(candidates)
    candidates[0] = 1000000
    candidates[1] = 1000000
    candidates[2] = 1000000

print(D[var])
