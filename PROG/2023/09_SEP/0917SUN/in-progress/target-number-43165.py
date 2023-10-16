class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def insertFirst(self, data):
        new_node = Node(data)
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < num:
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    def insertLast(self, data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next
        new_node = Node(data)
        node.next = new_node
        self.list_size += 1