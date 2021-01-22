import queue


def bfs(adj, source):
    visited = [0 for i in range(len(adj))]

    q = queue.Queue(maxsize=len(adj))

    q.put(source)
    visited[source] = 1

    while not q.empty():
        current_node = q.get()
        print(current_node, end=' ')

        for i in range(len(adj[current_node])):         # not a pythonic way
            adjacent_node = adj[current_node][i]
            if visited[adjacent_node] == 0:
                visited[adjacent_node] = 1
                q.put(adjacent_node)


n = int(input("Enter the number of nodes: "))
e = int(input("Enter the number of edges: "))

adj_list = [[] for i in range(n)]

print("Enter edges in separate lines.")
for i in range(e):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

s = int(input('Enter source vertex: '))
print('BFS: ', end="")
bfs(adj_list, s)
