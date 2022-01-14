class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.start_node = None

    # def insertToEmptyList(self, data):
    #     if self.start_node is None:
    #         new_node = Node(data)
    #         self.start_node = new_node

    def insertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    # def display(self):
    #     if self.start_node is None:
    #         print(" ")
    #         return
    #     else:
    #         n = self.start_node
    #         while n is not None:
    #             print(n.item, end=" ")
    #             n = n.next
    #         print("\n")

    def search(self, data):
        if self.start_node is None:
            print("0")
            return
        else:
            n = self.start_node
            counter = 0
            while n is not None:
                if n.item == data:
                    counter += 1
                n = n.next
            print(counter)

    def findNeighbor(self, value):
        n = self.start_node
        index = 0
        listOfNeighbors = []
        while n is not None:
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
for i in range(amountOfCommands):
    choice, var1, *_ = input().split()
    choice = int(choice)
    var1 = int(var1)
    var2 = int(*_)
    if choice == 1:
        newDoublyLinkedList.insertToEnd(var1)
        newDoublyLinkedList.insertToEnd(var2)
    elif choice == 4:
        newDoublyLinkedList.search(var1)
    elif choice == 5:
        newDoublyLinkedList.findNeighbor(var1)
