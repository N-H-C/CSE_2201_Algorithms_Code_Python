arr_1 = [1, 3, 5, 7, 9]
arr_2 = [2, 4, 6, 8, 10]
sorted_arr = [None] * len(arr_1 + arr_2)

i = 0
j = 0
k = 0

while i < len(arr_1) and j < len(arr_2):
    if arr_1[i] < arr_2[j]:
        sorted_arr[k] = arr_1[i]
        k += 1
        i += 1
    else:
        sorted_arr[k] = arr_2[j]
        k += 1
        j += 1

while i < len(arr_1):
    sorted_arr[k] = arr_1[i]
    k += 1
    i += 1

while j < len(arr_2):
    sorted_arr[k] = arr_2[j]
    k += 1
    j += 1

print(sorted_arr)