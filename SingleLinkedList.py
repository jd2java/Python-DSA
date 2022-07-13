class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.nextNode
        print("Null")

    def insertBegin(self, ele):
        temp = Node(ele)
        temp.nextNode = self.head
        self.head = temp

    def insertEnd(self, ele):
        temp = Node(ele)
        if self.head is None:
            return temp
        cur = self.head
        while cur.nextNode:
            cur = cur.nextNode
        cur.nextNode = temp

    def insertAtPosition(self, ele, position):
        if position < 1:
            print("Invalid position\n")
            return
        if position == 1:
            temp = Node(ele)
            temp.nextNode = self.head
            self.head = temp
        else:
            count = 0
            temp = Node(ele)
            cur = self.head
            while cur.nextNode is not None:
                cur = cur.nextNode
                count += 1
                if count == position - 1:
                    cur.nextNode = temp
                    temp.nextNode = cur.nextNode


if __name__ == '__main__':
    lList = SingleLinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(3)

    lList.head.nextNode = second
    second.nextNode = third

    # Printing the list
    # lList.printList()
    # print("\n")

    # Insert at the beginning of the linked list.
    print("The linked list after inserting at the beginning:")
    lList.insertBegin(25)
    lList.printList()
    print()

    # Insert at the end of the linked list.
    print("The linked list after inserting at the end:")
    lList.insertEnd(35)
    lList.printList()
    print()

    # Insert at a given position in the linked list.
    print("The linked list after inserting node at a given position:")
    lList.insertAtPosition(23, 2)
    lList.printList()
