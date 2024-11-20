class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.count = 0

    
    def append(self, data):
        if self.isFull():
            self.capacity = self.capacity * 2
            new_array = Array(self.capacity)
            for index in range(self.count):
                new_array.items[index] = self.items[index]
            self.items = new_array.items
        self.items[self.count] = data
        self.count += 1

    def insertAt(self, index, data):
        if index < 0 or index > self.count:
            print("Index out of bound")
            return
            

    def pop(self):
        if self.isEmpty():
            print("Array is empty. Can't delete")
            return
        self.items[self.count-1] = None
        self.count -= 1

    def indexOf(self, data):
        if self.isEmpty():
            print(-1)
            return -1
        for index in range(self.count):
            # print(index, self.items[index])
            if self.items[index] == data:
                print(index)
                return
        print("No data found")
        return
            

    def isFull(self):
        return self.count == self.capacity
    
    def isEmpty(self):
        return self.count == 0
    
    def printArray(self):
        for index in range(self.capacity):
            print(self.items[index], end="->")


arr = Array(5)
arr.pop()
arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)
arr.append(50)
arr.append(60)
arr.append(70)
arr.pop()
arr.pop()
arr.indexOf(30)
arr.indexOf(100)
arr.printArray()