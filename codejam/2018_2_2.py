
def exe(arr, add, start, end):

    for i in range(len(arr)):
        arr[i] = arr[i] + (i*add)

    for i in range(int((end-start+1)/2)):
        temp = arr[start+i]
        arr[start+i] = arr[end-i]
        arr[end-i] = temp

    # if (end - start) % 2 == 0:
    #     arr[int(start+((end-start)/2))] = int((start+((end-start)/2))*add)

n, q, m = input().split()

n = int(n)
q = int(q)
m = int (m)

arr = [0]*n

add = 0

for i in range(0,q):

    a = input().split()

    if a[0] == 'a':
        add = add + 1
        continue
    else:
        a[1] = int(a[1])
        a[2] = int(a[2])

        exe(arr, add, a[1], a[2])
        add = 0

b = input().split()

for i in b:
    print(arr[int(i)])
