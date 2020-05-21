# ???
def merge(arr, p, q, r):
    n1 = p - q + 1
    n2 = r - q

    L = arr[p: q + 1]
    R = arr[q + 1: r + 1]
    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)

        merge(arr, p, q, r)


a = input("Enter elements separated by space: ").split(' ')
arr = [int(i) for i in a]

merge_sort(arr, 0, len(arr) - 1)
print("Sorted array: ", arr)
