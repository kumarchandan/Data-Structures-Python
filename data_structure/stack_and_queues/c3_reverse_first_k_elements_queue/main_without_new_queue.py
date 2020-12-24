from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    if k > queue.size() or k < 0 or queue.is_empty():
        return None
    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())
    return queue

queue = MyQueue()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in data:
    queue.enqueue(i)

print('Queue:')
print(queue.queue_list)

print('After reversing elements:')
print(reverseK(queue, 5).queue_list)