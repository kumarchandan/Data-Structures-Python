'''
Given a singly linked list and an integer 'k', reverse every 'k' element. 
If k <= 1, then the input list is unchanged. If k >= n (n is the length of 
linked list), then reverse the whole linked list.
'''

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_every_k_nodes(head, k):
  if k <= 1 or head is None:
    return head

  current, previous = head, None
  while True:
    counter = 1
    last_node_of_prev_part = previous
    # after reversing current becomes last node
    last_node_of_curr_sublist = current

    while current and counter <= k:
      next = current.next
      current.next = previous
      previous = current
      current = next
      counter += 1
    
    # connect with the previous part
    if last_node_of_prev_part is None:
      head = previous
    else:
      last_node_of_prev_part.next = previous
    
    # connect with the next part
    last_node_of_curr_sublist.next = current

    if current is None:
      break
    previous = last_node_of_curr_sublist
    
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  # head.next.next.next.next.next.next.next = Node(8)
  # head.next.next.next.next.next.next.next.next = Node(9)
  # head.next.next.next.next.next.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_nodes(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
