def dfs(adj, visited, current_node):
    if current_node not in visited:
        visited.add(current_node)

        for neighbour in adj[current_node]:
            if neighbour not in visited:
                dfs(adj, visited, neighbour)

        print(current_node, end=' ')


n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

adj_list = {}

undirected_graph = input("Undirected graph? (Y/N) ")
print("Enter edges (u, v) in separate line(s).")
for i in range(e):
    u, v = input().split()
    adj_list[u] = v
    if undirected_graph == 'Y' or undirected_graph == 'y':
        adj_list[v] = u

visited = set()

print("DFS: ", end='')
for vertex in adj_list:
    if vertex not in visited:
        dfs(adj_list, visited, vertex)
