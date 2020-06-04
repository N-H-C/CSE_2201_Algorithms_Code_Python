from math import inf

p = input("Enter matrix dimensions' array separated by space: ").split(" ")
p = [int(i) for i in p]
n = len(p) - 1

table = [[inf for i in range(n + 1)] for i in range(n + 1)]
for i in range(n + 1):
    table[i][i] = 0

s = [[-1 for i in range(n + 1)] for i in range(n + 1)]

for L in range(2, n + 1):
    for i in range(1, n - L + 2):
        j = i + L - 1
        # table[i][j] = inf
        for k in range(i, j):
            q = table[i][k] + table[k + 1][j] + p[i - 1] * p[k] * p[j]
            if q < table[i][j]:
                table[i][j] = q
                s[i][j] = k

print("Total operation: ", table[1][n])


def print_parentheses(s, i, j):
    if i == j:
        print("A%d" % i, end="")
    else:
        print("(", end="")
        print_parentheses(s, i, s[i][j])
        print_parentheses(s, s[i][j] + 1, j)
        print(")", end="")


print("Multiplication order: ", end="")
print_parentheses(s, 1, n)
