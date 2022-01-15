def addVertex(v):
  global graph
  global vertices_no
  if v not in graph:
    vertices_no = vertices_no + 1
    graph[v] = []

def addEdge(v1, v2):
  global graph
  if v1 in graph and v2 in graph:
    temp = v2
    graph[v1].append(temp)

def bfs(visited, graph, node, result):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0)
    result.append(s)
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

amountOfCities, amountOfRoads = input().split()
amountOfCities = int(amountOfCities)
amountOfRoads = int(amountOfRoads)
graph = {}
vertices_no = 0
visited = []
queue = []
for i in range(amountOfCities):
    addVertex(i)

for j in range(amountOfRoads):
    cityA, cityB = input().split()
    cityA = int(cityA)
    cityB = int(cityB)
    addEdge(cityA, cityB)
    addEdge(cityB, cityA)

print(graph)
result = []
bfs(visited, graph, 0, result)
result.reverse()
print(*result, sep= " ")