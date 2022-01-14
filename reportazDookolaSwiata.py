amountOfCities, amountOfCommands = input().split()
amountOfCities = int(amountOfCities)
amountOfCommands = int(amountOfCommands)
connectionsMatrix = []
commandsMatrix = []
amountOfConnections = 0
for i in range(amountOfCommands):
    choice, var1, *_ = input().split()
    commandsMatrix.append(choice, var1, *_)

print(commandsMatrix)