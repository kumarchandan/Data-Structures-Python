from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    #
    if k > queue.size() or k < 0 or queue.is_empty():
        return None
    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    queue_new = MyQueue()
    while stack.is_empty() is False:
        queue_new.enqueue(stack.pop())
    while queue.is_empty() is False:
        queue_new.enqueue(queue.dequeue())
    return queue_new

queue = MyQueue()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in data:
    queue.enqueue(i)

print('Queue:')
print(queue.queue_list)

print('After reversing elements:')
print(reverseK(queue, 5).queue_list)