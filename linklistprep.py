class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        Now_node = self.head
        while True:
            if Now_node is None:
                break
            print(Now_node.data)
            Now_node = Now_node.next


k = Node("john")
l1 = LinkedList()
l1.insert(k)
h = Node("Ben")
l1.insert(h)
l1.printList()

LinkedList.printList(l1)
