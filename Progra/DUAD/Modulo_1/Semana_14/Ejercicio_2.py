class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleEndedQueue:
    def __init__(self):
        self.right = None
        self.left = None

    def print(self):
        current = self.left
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("None")

    def push_right(self, data):
        new_node = Node(data)
        if self.right is None:
            self.right = new_node
            self.left = new_node
        else:
            self.right.next = new_node
            new_node.prev = self.right
            self.right = new_node

    def push_left(self, data):
        new_node = Node(data)
        if self.left is None:
            self.right = new_node
            self.left = new_node
        else:
            self.left.prev = new_node
            new_node.next = self.left
            self.left = new_node

    def pop_right(self):
        if self.right is None:
            raise IndexError("Empty queue")

        data = self.right.data
        self.right = self.right.prev

        if self.right is not None:
            self.right.next = None
        
        else:
            self.left = None

        return data
    
    def pop_left(self):
        if self.left is None:
            raise IndexError("Empty queue")
        data = self.left.data
        self.left = self.left.next

        if self.left is not None:
            self.left.prev = None

        else:
            self.right = None

        return data



first_queue = DoubleEndedQueue()

first_queue.push_right("First")
first_queue.push_right("Second")

first_queue.print()

print("-----------------")

first_queue.push_left("Third")
first_queue.push_left("Fourth")

first_queue.print()

print("-----------------")

print("popped Right:" , first_queue.pop_right())
first_queue.print()

print("popped Left:" , first_queue.pop_left())
first_queue.print()