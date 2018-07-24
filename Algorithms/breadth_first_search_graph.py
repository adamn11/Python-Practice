def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                queue.append(neighbor)
    return visited

def main():
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A','D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B','D'],
             'F': ['C'],
             'G': ['C']}
    print(bfs(graph, 'A'))

if __name__ == "__main__":
    main()