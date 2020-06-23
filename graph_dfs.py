import queue


def dfs(adj, visited, current_node):
    if visited[current_node] != 0:
        return

    visited[current_node] = 1

    for i in range(len(adj[current_node])):  # not a pythonic way
        adjacent_node = adj[current_node][i]
        if visited[adjacent_node] == 0:
            dfs(adj, visited, adjacent_node)

    print(current_node, end=' ')


n = int(input("Enter the number of nodes: "))
e = int(input("Enter the number of edges: "))

adj_list = [[] for i in range(n)]

print("Enter edges in separate lines.")
for i in range(e):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [0 for i in range(n)]
print('DFS: ', end="")
for i in range(n):
    if visited[i] == 0:
        dfs(adj_list, visited, i)
