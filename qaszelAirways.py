amountOfCities, amountOfCommands = input().split()
amountOfCities = int(amountOfCities)
amountOfCommands = int(amountOfCommands)
connectionsMatrix = [[0 for x in range(amountOfCities)] for y in range(amountOfCities)]
for i in range(amountOfCommands):
    choice, var1, *_ = input().split()
    choice = int(choice)
    var1 = int(var1)
    var2 = int(*_)
    if choice == 1:
        connectionsMatrix[var1][var2] = 1
        connectionsMatrix[var2][var1] = 1
    elif choice == 2:
        connectionsMatrix[var1][var2] = 0
        connectionsMatrix[var2][var1] = 0
    elif choice == 3:
        if connectionsMatrix[var1][var2] == 1:
            print("TAK")
        else:
            print("NIE")
    elif choice == 4:
        amountOfConnections = 0
        for j in range(amountOfCities):
            if connectionsMatrix[var1][j] == 1:
                amountOfConnections += 1
        print(amountOfConnections)