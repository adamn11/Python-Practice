class Graph:
    def __init__(self):
        self._graph = {}

    def print_graph(self):
        return self._graph

    def get_vertices(self):
        return list(self._graph.keys())

    def get_edges(self):
        for vertices in self._graph.keys():
            for neighbors in vertices:
                print(neighbors)

    def get_size(self):
        return len(list(self._graph.keys()))

    def add_vertex(self, value):
        self._graph[value] = []

    def add_edges(self, u, v):
        if u not in self.get_vertices():
            self.add_vertex(u)
        if v not in self.get_vertices():
            self.add_vertex(v)
        self._graph[u].append(v)
        self._graph[v].append(u)

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            popped = stack.pop()

            if popped not in visited:
                visited.append(popped)
                neighbors = self._graph[popped]

                for neighbor in neighbors:
                    stack.append(neighbor)

        return visited

    def bfs(self, start):
        visited = []
        queue = [start]

        while queue:
            popped = queue.pop(0)

            if popped not in visited:
                visited.append(popped)
                neighbors = self._graph[popped]

                for neighbor in neighbors:
                    queue.append(neighbor)

        return visited


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_edges('A', 'B')
    g.add_edges('C', 'A')
    print('Graph: %s' % g.print_graph())
    print('Size: %s' % g.get_size())
    print('DFS: %s' % g.dfs('A'))
    print('BFS: %s' % g.bfs('A'))
