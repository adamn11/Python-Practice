def bfs(graph, start):
    visited = []  # A list to keep track of all the nodes that have been visited
    queue = [start]  # BFS uses a queue, with the start node already appended

    # Goes through all nodes in queue before finishing
    while queue:
        node = queue.pop(0)

        # If the node has not been visited...
        if node not in visited:
            # Mark as visited...
            visited.append(node)
            neighbors = graph[node]

            # Then go through all nodes connected and append to queue
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