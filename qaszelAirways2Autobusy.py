# Pierwsza linia wejścia składa się z dwóch liczb, n i m. W kolejnych m liniach znajdują się komendy. Możliwe komendy to:
# 1 A B - dodanie (dwukierunkowego) połączenia z A do B
# 4 A - pytanie o liczbę połączeń z A
# 5 A - pytanie o listę miast, do których można bezpośrednio dostać się z A
# Złożoność programu nie powinna być gorsza niż O(p log(n)+n),
# gdzie p to łączna liczba liczb, które znajdują się na wejściu oraz w prawidłowym wyjściu programu, a n to ilość miast.
# Program należy wykonać z użyciem listy.

class Node:
    def __init__(self, data):                                       #tworze listę dwukierunkową, ze zmiennymi wartości, następnej komórki i poprzedniej komórki, O(1)?
        self.item = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.start_node = None

    def insertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:                                   #dodanie elementu na koniec listy, pojawia się while więc O(n)?
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n


    def search(self, data):
        if self.start_node is None:
            print("0")
            return
        else:
            n = self.start_node
            counter = 0
            while n is not None:                                    #w przeszukiwaniu listy sprawdzam każdy element więc znowu O(n)
                if n.item == data:
                    counter += 1
                n = n.next
            print(counter)

    def findNeighbor(self, value):
        n = self.start_node
        index = 0
        listOfNeighbors = []
        while n is not None:                                        #w znajdowaniu elementów sąsiednich też przeszukuję całą listę więc znowu O(n)
            index += 1
            if index % 2 != 0:
                if n.item == value:
                    listOfNeighbors.append(n.next.item)
            else:
                if n.item == value and n is not None:
                    listOfNeighbors.append(n.prev.item)
            n = n.next
        listOfNeighbors.sort()
        print(*listOfNeighbors, sep=" ")



amountOfCities, amountOfCommands = input().split()
amountOfCities = int(amountOfCities)
amountOfCommands = int(amountOfCommands)
newDoublyLinkedList = DoublyLinkedList()
for i in range(amountOfCommands):                                           #for, czyli złożoność to p?
    choice, var1, *_ = input().split()
    choice = int(choice)
    var1 = int(var1)
    var2 = int(*_)
    if choice == 1:                                                         #dodanie dwóch elementów na koniec listy
        newDoublyLinkedList.insertToEnd(var1)
        newDoublyLinkedList.insertToEnd(var2)
    elif choice == 4:                                                       #znalezienie w liście wystąpień danego elementu O(n)?
        newDoublyLinkedList.search(var1)
    elif choice == 5:                                                       #znajdowanie miast sąsiadujących ze sobą w liście - połączeń O(n)?
        newDoublyLinkedList.findNeighbor(var1)
                                                                            #tak na prawdę, nie wiem jaka jest złożoność po wykonaniu wszystkich komend, ale chyba p*n^2

#Sprawdzarka pokazuje mi, że kod spełnia wymogi w 40%

