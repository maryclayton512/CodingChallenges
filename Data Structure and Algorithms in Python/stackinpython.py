"""
Name: Mary Clayton
Date: 7/20/2022
Purpose: Stack Data Structure

"""
# Class
class Stack():
    # constructor
    def __init__(self):
        self.items = []

    # Methods
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items
        
# Declare class as a object
myStack = Stack()
# Push book A and B
myStack.push("A")
myStack.push("B")
# Print the get stack method
print(myStack.get_stack())
# Push Book C
myStack.push("C")
# Print the get stack method again
print(myStack.get_stack())
# Pop the last element of the list
myStack.pop()
# Print get stack method for a third time
print(myStack.get_stack())

# Testing whether list is empty or not
# print(myStack.is_empty())
# Taking a peek at last element in list
# print(myStack.peek())

