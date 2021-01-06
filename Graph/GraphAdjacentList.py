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
            
        curr_conn_list = self.adjacentList[node1]
        curr_conn_list.add(node2)
        self.adjacentList[node1] = curr_conn_list

        curr_conn_list = self.adjacentList[node2]
        curr_conn_list.add(node1)
        self.adjacentList[node2] = curr_conn_list

    def show_connections(self):
        pass
