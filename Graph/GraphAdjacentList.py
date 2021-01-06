class Graph:

    def __init__(self):
        self.NumberOfNodes = 0
        self.adjacentList = {}

    def __repr__(self):
        return str(self.adjacentList)

    def add_vertex(self, node):
        self.adjacentList[node] = set()
        self.NumberOfNodes += 1

    def add_edge(self, node1, node2):
        if node1 == node2:
            return
        if node1 not in self.adjacentList.keys():
            self.add_vertex(node1)
        if node2 not in self.adjacentList.keys():
            self.add_vertex(node2)

        self.adjacentList[node1].add(node2)
        self.adjacentList[node2].add(node1)


# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)

print(g)
