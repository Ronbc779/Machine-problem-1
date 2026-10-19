#202505496
from lab1_solution import Array, SLLNode

class ArrayStack:
    def __init__(self, capacity = 10):
        self.array = Array(capacity)
        self.size = 0


    def __repr__(self):
        #string representation of stack using array
        if self.is_empty():
            print("Top ->[Stack is empty]")
            return
        items = self.array.items[:self.size]
        display = ", ".join(str(x) for x in items[::-1])
        return 'Top ->[' + display + ']'

    def is_empty(self):
        #check if stack is empty
        if self.size == 0:
            return True
        else:
            return False

    def push(self, item):
        #checks if array is full then expand if it is
        if self.size == self.array.capacity:
            self.array.expand(self.array.capacity * 2)
        #then add item to stack
        self.array[self.size] = item
        self.size = self.size + 1

    def pop(self):
        #check if empty before popping
        if self.is_empty():
            raise Exception('Empty stack: cannot pop')
        else:
            item = self.array.items[self.size - 1]
            self.array.items[self.size - 1] = None
            self.size = self.size - 1
            return item

    def top(self):
        #view the top
        if self.size == 0:
            raise Exception("Stack is empty")
        return self.array[self.size - 1]

class SLLStack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def __repr__(self):
        #string representation of stack using SLLNodes
        if self.is_empty():
            return "Top -> <EMPTY STACK>"
        curr = self.top_node
        items = []
        while curr != None:
            items.append('<' + str(curr.get_item()) + '>')
            curr = curr.get_next()
        display = ", ".join(str(x) for x in items)
        return 'top ->' + display

    def is_empty(self):
        #check if stack is empty
        if self.size == 0:
            return True
        else:
            return False

    def push(self, item):
        #insert at front algorithm
        new_node = SLLNode(item)
        new_node.set_next(self.top_node)
        self.top_node = new_node
        self.size = self.size + 1

    def pop(self):
        #set the top node to the next of the old top node
        if self.size == 0:
            raise Exception('Empty stack: cannot pop')
        old_top_item = self.top_node.get_item()
        old_top = self.top_node
        self.top_node = self.top_node.get_next()
        old_top.set_next(None)
        self.size = self.size - 1
        return old_top_item

    def top(self):
        #view top
        if self.size == 0:
            raise Exception('Empty stack: no top')
        return self.top_node.get_item()

    
# array = ArrayStack()
# array.push('P')
# array.push('E')
# print(array)
# print(array.top())
# print(array.pop())
# print(array.is_empty())
# print(array.pop())
# print(array.is_empty())

# stack = SLLStack()
# stack.push('P')
# print(stack.is_empty())
# print(stack)
# print(stack.top())
# stack.push('E')
# print(stack.pop())
# stack.push('T')
# print(stack)
# stack.pop()
# print(stack)
# print(stack.pop())
# print(stack)