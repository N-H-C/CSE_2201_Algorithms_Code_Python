def linear_search_1(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1


def linear_search_2(arr, x):
    if x in arr:
        return arr.index(x)

    return -1


a = [1, 3, 4, 5, 8]
number = 8
index = linear_search_2(a, number)
print("Element found at index ", index)

# Input N numbers from the user METHOD 1 (enter inputs in separate lines)
a = list()
n = int(input("Number of elements: "))
for i in range(n):
    num = int(input())
    a.append(num)

print("List: ", a)
number = int(input("Enter the searching value: "))
index = linear_search_2(a, number)
print("Element found at index ", index)


# Input N numbers from the user METHOD 2
a = input("Enter elements separated by space: ").split(' ')
a_list = [int(i) for i in a]
print(a_list)
