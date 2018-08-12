import sys

D = [0]*301
flr = [0]*301
flg = [0]*301

cnt = int(sys.stdin.readline())

for idx in range(1, cnt+1):
    flr[idx] = int(sys.stdin.readline())


print(flr)


D[1] = flr[1]
D[2] = flr[1] + flr[2]
D[3] = max(flr[1]+flr[3], flr[2]+flr[3])

for idx in range(4, cnt+1):

    if flg[idx-1] is True:



#print(D[var])
