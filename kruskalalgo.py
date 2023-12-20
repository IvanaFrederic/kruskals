class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def kruskal(self):
        # Sort the edges by weight in ascending order
        self.graph.sort(key=lambda edge: edge[2])

        parent = {}

        def find_set(vertex):
            if vertex not in parent:
                parent[vertex] = vertex
            elif vertex != parent[vertex]:
                parent[vertex] = find_set(parent[vertex])
            return parent[vertex]

        def union_sets(root1, root2):
            parent[root1] = root2

        min_spanning_tree = []

        for edge in self.graph:
            u, v, weight = edge
            root_u = find_set(u)
            root_v = find_set(v)

            if root_u != root_v:
                min_spanning_tree.append(edge)
                union_sets(root_u, root_v)

        return min_spanning_tree

# Example usage:
g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 4)
g.add_edge('C', 'D', 5)

min_spanning_tree = g.kruskal()

print("Minimum Spanning Tree using Kruskal's Algorithm:")
for edge in min_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
