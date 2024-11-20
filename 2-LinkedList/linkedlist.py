class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def addLast(self, data):
        new_node = Node(data)
        if not self.isEmpty():
            self.tail.next = new_node
            self.tail = new_node
            return
        self.addFirst(data)
        
    def deleteFirst(self):
        if not self.isEmpty():
            self.head = self.head.next
        return

    def deleteLast(self):
        if self.isEmpty():
            return
        current_node = self.head
        while current_node != None and current_node.next.next != None:
            current_node = current_node.next
        self.tail = current_node
        current_node.next = None

    def contains(self, data):
        if self.indexOf(data) != -1:
            return True
        return False

    def indexOf(self, data):
        if self.isEmpty():
            return -1
        current_node = self.head
        count = 0
        while current_node != None and current_node.data != data:
            current_node = current_node.next
            count += 1
        return count if current_node is not None else -1
    
    def isEmpty(self):
        return self.head == None

    def printLL(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print()


ll = LinkedList()
ll.addFirst(10)
ll.addFirst(20)
ll.addFirst(30)
ll.addLast(100)
ll.addLast(200)
ll.addLast(300)
# ll.deleteFirst()
# ll.deleteFirst()
ll.deleteLast()
ll.deleteLast()
ll.deleteLast()
print(ll.indexOf(20))
ll.printLL()
print(ll.contains(10343))
print(ll.contains(20))