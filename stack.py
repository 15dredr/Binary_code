class Stack:
    def __init__(self):
        self.data = []

    def push(self, g):
        self.data = [g] + self.data

    def pop(self):
        value_to_return = self.data[0]
        del self.data[0]
        return value_to_return

    @property
    def top(self):
        if self.empty == True:
            return None
        else:
            return self.data[0]

    @property
    def size(self):
        return len(self.data)

    @property
    def empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False


my_stack = Stack()
my_stack.push("Grade papers")
my_stack.push("Enter grades")
my_stack.push("Sort letters")
while not my_stack.empty:

