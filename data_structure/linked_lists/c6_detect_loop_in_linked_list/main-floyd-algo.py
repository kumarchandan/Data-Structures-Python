'''
This is perhaps the fastest algorithm for detecting a linked list loop. We keep 
track of two iterators, onestep and twostep.

onestep moves forward one node at a time, while twostep iterates over two nodes. In this way, 
twostep is the faster iterator.

By principle, if a loop exists, the two iterators will meet. Whenever this condition is 
fulfilled, the function returns True.
'''

from LinkedList import LinkedList
# Floyd's Cycle Finding Algorithm
def detect_loop(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element  # Moves one node at a time
        twostep = twostep.next_element.next_element  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False

# ----------------------


lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

# Adding a loop
head = lst.get_head()
node = lst.get_head()

for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop(lst))
