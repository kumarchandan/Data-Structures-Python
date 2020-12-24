'''
Create an efficient min() function using a stack
'''
from Stack import MyStack
# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()

class MinStack:
    # Constructor
    def __init__(self):
        # Write your code here
        self.main_stack = MyStack()
        self.min_stack = MyStack()
        return None

    # Removes and return value from newStack
    def pop(self):
        value = self.main_stack.pop()
        self.min_stack.pop()
        return value

    # Pushes values into newStack
    def push(self, value):
        # Push to the main_stack
        self.main_stack.push(value)
        
        if self.min_stack.is_empty() or self.min_stack.top() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())

    # Returns minimum value from newStack in O(1) Time
    def min(self):
        if self.min_stack.is_empty():
            return None
        else:
            return self.min_stack.top()


stack = MinStack()
stack.push(5)
stack.push(6)
stack.push(2)
stack.push(4)
stack.push(10)
stack.push(1)

print(stack.main_stack.stack_list)
print("minimum value: " + str(stack.min()))

stack.pop()
print(stack.main_stack.stack_list)
print("minimum value: " + str(stack.min()))