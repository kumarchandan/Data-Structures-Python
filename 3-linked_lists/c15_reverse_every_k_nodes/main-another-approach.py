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
  # if k is 0 or 1, then list is not changed
  if k <= 1 or head is None:
    return head

  reverse = None
  prev_tail = None

  while head and k > 0:
    current_head = None
    current_tail = head

    n = k
    while head and n > 0:
      temp = head.next
      head.next = current_head
      current_head = head

      head = temp
      n -= 1

    if reverse is None:
      reverse = current_head

    if prev_tail:
      prev_tail.next = current_head

    prev_tail = current_tail

  return reverse

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