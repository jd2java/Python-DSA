class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break

    def insertFront(self, ele):
        new_node = Node(ele)
        temp = self.head

        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def insertEnd(self, ele):
        new_node = Node(ele)
        temp = self.head
        new_node.next = temp
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node

    def deleteEnd(self):
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        temp = self.head
        temp.next.next = None

    def insertPosition(self, ele, pos):
        temp = Node(ele)
        cur = self.head
        pos -= 1
        while pos != 1:
            cur = cur.next
            pos -= 1
        temp.next = cur.next
        cur.next = temp


if __name__ == '__main__':
    lList = CircularSinglyLinkedList()
    # Insert at begin
    lList.insertFront(23)
    lList.insertFront(34)

    # Printing the list
    print("Original List:")
    lList.printList()
    print()

    # Insert at the end of the linked list.
    print("The linked list after inserting at the end")
    lList.insertEnd(45)
    lList.printList()
    print()

    # Delete end node from the linked list.
    print("The linked list after deleting at the end")
    lList.deleteEnd()
    lList.printList()
    print()

    # Insert at a given position of the linked list.
    print("The linked list after inserting at specified position")
    lList.insertPosition(77, 2)
    lList.printList()
    print()
