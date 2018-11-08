# def exe(arr, add, start, end):
#
#     for i in range(int((end-start+1)/2)):
#         temp = arr[start+i]
#         arr[start+i] = (end-i)*add + arr[end-i]
#         arr[end-i] = (start+i)*add + temp
#
#     if (end - start) % 2 == 0:
#         arr[int(start+((end-start)/2))] = int((start+((end-start)/2))*add)


li = [0, 3, 4]

for i in li:
    print(i)