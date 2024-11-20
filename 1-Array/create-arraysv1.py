from typing import Any

class Array:
    def __init__(self, capacity: int) -> None:
        """_summary_

        Args:
            capacity (int): _description_
        """
        self.capacity = capacity
        self.items = [None] * capacity
        self.count = 0

    def _isFull(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        return self.count == self.capacity

    def append(self, data: Any) -> None:
        """_summary_

        Args:
            data (Any): _description_
        """
        if self._isFull():
            self.capacity = 2 * self.capacity
            new_array = Array(self.capacity)
            for i in range(self.count):
                new_array.items[i] = self.items[i]
            self.items = new_array.items
        self.items[self.count] = data
        self.count += 1

    def insertAt(self, index: int, data: Any) -> None:
        """_summary_

        Args:
            index (int): _description_
            data (Any): _description_
        """
        if index < 0 or index >= self.count:
            print("List index out of bounds")
            return
        
        if self.count == self.capacity:
            pass

        for i in range(self.count, index, -1): #5  -  2
            self.items[i] = self.items[i-1]
        self.items[index] = data
        self.count += 1

    def pop(self) -> Any:
        """_summary_

        Returns:
            Any: _description_
        """
        if self.isEmpty():
            print("Empty Array! Not able to delete")
            return
        data = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -= 1
        return data

    def delete(self, data: Any) -> None:
        """_summary_

        Args:
            data (Any): _description_
        """
        if self.isEmpty():
            print("Empty Array! Not able to delete")
            return
        position = self.indexOf(data)

        if position == self.count - 1:
            self.pop()
            self.count -= 1

        if position != -1:
            for i in range(position, self.count):
                self.items[i] = self.items[i+1]
            self.count -= 1
        else:
            print("No element found to delete")

    def isEmpty(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        return self.count == 0
    
    def indexOf(self, data: Any) -> int:
        """_summary_

        Args:
            data (Any): _description_

        Returns:
            int: _description_
        """
        for i in range(self.count):
            if self.items[i] == data:
                print(i)
                return(i)
        return -1

    def printArray(self) -> None:
        """_summary_
        """
        for i in range(self.capacity):
            print(self.items[i], end="->")

    def maxElement(self):
        if not self.isEmpty():
            big = self.items[0]
            for i in range(1, self.count):
                if self.items[i] > big:
                    big = self.items[i]
            print(big)
            return big 
        print("Array is empty")
        return "Array is empty"
    
    def intersect(self, new_array):
        if self.isEmpty():
            return None
        for i in self.items:
            for j in new_array:
                if i == j:
                    print(i, end=" ")
        print()
    
    def reverse(self):
        for i in range(self.count, -1, -1):
            print(self.items[i], end="->")


arr = Array(capacity=5)
arr.pop()
arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)
arr.append(50)
print("**************************")
arr.printArray()
arr.append(60)
arr.append(70)
print("**************************")
arr.printArray()
arr.insertAt(2, 100)
# arr.delete(10)
# arr.delete(20)
# arr.delete(70)
# arr.delete(0)
# arr.pop()
# arr.indexOf(10)
# arr.indexOf(20)
arr.delete(50)
arr.printArray()

