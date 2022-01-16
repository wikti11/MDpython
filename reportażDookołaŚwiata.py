class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, src, des):
        self.adj[src].append(des)
        self.adj[des].append(src)

    def minEdgeDFSUtil(self, visited, src, des, min_num_of_edges, edge_count):
        visited[src] = True
        if src == des:
            if min_num_of_edges > edge_count:
                min_num_of_edges = edge_count
        else:
            for v in self.adj[src]:
                if not visited[v]:
                    edge_count += 1
                    min_num_of_edges, edge_count = \
                        self.minEdgeDFSUtil(visited, v, des, min_num_of_edges, edge_count)
        visited[src] = False
        edge_count -= 1
        return min_num_of_edges, edge_count

    def minEdgeDFS(self, u, v):
        visited = [False] * self.V
        min_num_of_edges = float('inf')
        edge_count = 0
        min_num_of_edges, edge_count = \
            self.minEdgeDFSUtil(visited, u, v, min_num_of_edges, edge_count)
        return min_num_of_edges


if __name__ == "__main__":
    amountOfCities, amountOfRoads = input().split()
    amountOfCities = int(amountOfCities)
    amountOfRoads = int(amountOfRoads)
    g = Graph(amountOfCities)
    listOfConnections = [0]
    connectionsMatrix = [[0 for x in range(amountOfCities)] for y in range(amountOfCities)]

    for i in range(amountOfRoads):
        cityA, cityB = input().split()
        cityA = int(cityA)
        cityB = int(cityB)
        g.addEdge(cityA, cityB)

    for j in range(amountOfCities):
        if g.minEdgeDFS(0, j) != 0:
            for k in range(g.minEdgeDFS(0, j)):
                listOfConnections.append(j)
    sortedList = sorted(listOfConnections, key=listOfConnections.count)
    anotherList = list(dict.fromkeys(sortedList))
    anotherList.reverse()
    print(*anotherList, sep=" ")