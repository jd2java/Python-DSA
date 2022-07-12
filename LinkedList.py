class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
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


if __name__ == '__main__':
    lList = LinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(3)

    lList.head.nextNode = second
    second.nextNode = third

    # Printing the list
    lList.printList()

    # Insert at the beginning of the linked list.
    print("The linked list after inserting at the beginning:\n")
    lList.insertBegin(25)
    lList.printList()

    # Insert at the end of the linked list.
    print("The linked list after inserting at the end:\n")
    lList.insertEnd(35)
    lList.printList()
