class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self):
        self.top = None

    def print(self):
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next

    def push(self, data: str):
        self.top = Node(data, self.top)

    def pop(self) -> str:
        if self.top is None:
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        return data



first_stack = Stack()

first_stack.push("first")
first_stack.push("Second")
first_stack.push("Third")
first_stack.push("Forth")

first_stack.print()

print("-------------------")

first_stack.pop()

first_stack.print()

print("-------------------")

first_stack.pop()

first_stack.print()

print("-------------------")

first_stack.pop()

first_stack.print()

