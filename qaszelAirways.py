#Pierwsza linia wejścia składa się z dwóch liczb, n i m. Następnie w kolejnych m liniach znajdują się komendy. Możliwe komendy to:
# 1 A B - dodanie połączenia z A do B
# 2 A B - usunięcie połączenia z A do B
# 3 A B - pytanie o to, czy istnieje połączenie z A do B
# 4 A - pytanie o liczbę połączeń z A
# Złożoność programu nie powinna być gorsza niż O(n^2+m), gdzie n to liczba miast, a m to liczba komend.
# Program należy wykonać z użyceim macierzy.

def countAmountOfConnections(matrix, value):
    amountOfConnections = 0
    for row in matrix:
        for element in row:
            if element == value:
                amountOfConnections += 1
    print(amountOfConnections)                                                      #złożoność tutaj to O(n^2)

amountOfCities, amountOfCommands = input().split()                                  #zczytywanie ilości miast i komend
amountOfCities = int(amountOfCities)
amountOfCommands = int(amountOfCommands)
connectionsMatrix = []
amountOfConnections = 0
for i in range(amountOfCommands):                                                   #ma być tyle wejść z konsoli ile ilości komend, więc pojawia się for i złożoność zwiększa się do m
    choice, var1, *_ = input().split()
    choice = int(choice)
    var1 = int(var1)
    var2 = int(*_)
    if choice == 1:                                                                 #dodanie połączenia, z tego co wiem to jest O(1)
        if [var1, var2] not in connectionsMatrix:
            connectionsMatrix.append([var1, var2])
    elif choice == 2:                                                               #usunięcie połączenia, z tego co wiem to też jest O(1)
        connectionToDelete = [var1, var2]
        if connectionsMatrix and connectionToDelete in connectionsMatrix:
            connectionsMatrix.remove(connectionToDelete)
    elif choice == 3:                                                               #przeszukanie macierzy/tablicy, czyli O(n), więc złożoność tutaj to O(m*n)
        connectionToLookup = [var1, var2]
        if connectionToLookup in connectionsMatrix:
            print("TAK")
        else:
            print("NIE")
    elif choice == 4:
        countAmountOfConnections(connectionsMatrix, var1)                           #tutaj zliczam elementy w macierzy (wiersze 1-7), więc złożoność wzrasta do O(n^2*m)

#Sprawdzarka pokazuje mi, że kod spełnia wymogi w 20%