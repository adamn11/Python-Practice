def dfs(graph, start):
    visited = []  # A list to keep track of all the nodes that have been visited
    stack = [start]  # DFS uses a stack, with the start node already appended

    while stack:
        # Pop the top of the stack
        popped = stack.pop()

        # If the node has not been visited...
        if popped not in visited:
            # Mark as visited then...
            visited.append(popped)
            neighbor = graph[popped]

            # Then go through all nodes connected and append to stack
            for neighbor in neighbors:
                stack.append(neighbor)

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