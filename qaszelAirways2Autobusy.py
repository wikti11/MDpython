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

def bfsList(graph, value):
    listOfThem = []
    for vertex in graph:
        if vertex == value:
            listOfThem = graph[value]
    listOfThem.sort()
    print(*listOfThem, sep=" ")

def bfsAmount(graph, value):
    listOfThem = []
    for vertex in graph:
        if vertex == value:
            listOfThem = graph[value]
    print(len(listOfThem))

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
    choice, var1, *_ = input().split()
    choice = int(choice)
    var1 = int(var1)
    var2 = int(*_)
    if choice == 1:
        addEdge(var1, var2)
        addEdge(var2, var1)
    if choice == 4:
        bfsAmount(graph, var1)
    if choice == 5:
        bfsList(graph, var1)