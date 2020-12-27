from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here
        self.second_stack = MyStack()

        # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        self.main_stack.push(value)

        # Removes Element From Queue
    def dequeue(self):
        # Take out the values from the main_stack and fill them to second_stack
        while self.main_stack.is_empty() is False:
            self.second_stack.push(self.main_stack.pop())
        # Value to be dequeued
        value = self.second_stack.pop()
        # Fill the main stack back with rest of the values
        while self.second_stack.is_empty is False:
            self.main_stack.push(self.second_stack.pop())
        return value
