from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def detect_loop(lst): # O(n^2)
  # Write your code here
  visited = []
  is_loop = False
  
  curr = lst.get_head()
  while curr: # O(n)
    if curr in visited: # O(n)
      is_loop = True
      return is_loop
    else:
      visited.append(curr)
    curr = curr.next_element
  return is_loop


lst = LinkedList()
lst.insert_at_head(7)
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.print_list()

print(detect_loop(lst))