class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end="->")
                temp = temp.next
        print("Null")

    def insertBegin(self, ele):
        temp = Node(ele)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertEnd(self, ele):
        temp = Node(ele)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = temp
        temp.prev = cur

    def deleteBegin(self):
        cur = self.head
        cur = cur.next
        self.head = cur
        cur.prev = None

    def deleteEnd(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        curPrev = cur.prev
        curPrev.next = None


if __name__ == '__main__':
    lList = DoublyLinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(3)

    lList.head.next = second
    second.prev = lList.head
    second.next = third
    third.prev = second

    # Display Original List
    print("Original List")
    lList.printList()
    print()

    # Insert at the beginning of doubly linked list
    print("The linked list after inserting a node at the beginning of the doubly linked list")
    lList.insertBegin(34)
    lList.printList()
    print()

    # Insert at the end of the doubly linked list
    print("The linked list after inserting a node at the end of the doubly linked list")
    lList.insertEnd(54)
    lList.printList()
    print()

    # Delete from the front of the doubly linked list.
    print("The linked list after deleting a node from the front of the doubly linked list")
    lList.deleteBegin()
    lList.printList()
    print()

    # Delete from the end of the doubly linked list.
    print("The linked list after deleting a node at the end of the doubly linked list")
    lList.deleteEnd()
    lList.printList()
