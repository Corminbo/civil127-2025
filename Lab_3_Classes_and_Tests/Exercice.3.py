class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.min_stack = []

    def push(self, value: int):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack")
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def max(self) -> int:
        if not self.max_stack:
            raise IndexError("max from empty stack")
        return self.max_stack[-1]

    def min(self) -> int:
        if not self.min_stack:
            raise IndexError("min from empty stack")
        return self.min_stack[-1]

# Exemple d'utilisation
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(5)
    print(s.max())  # devrait afficher 5
    s.push(9)
    print(s.pop())  # devrait afficher 9
    s.push(2)
    print(s.max())  # devrait afficher 5
    print(s.min())  # devrait afficher 1