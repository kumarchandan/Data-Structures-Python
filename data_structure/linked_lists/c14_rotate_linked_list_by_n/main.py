# TODO: Not working with negative values
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

def find_length(head):
  # Calculate length of the Linked List
    length = 0
    while head:
        length += 1
        head = head.next

    return length

def adjust_rotations_needed(n, length):
  # If n is positive then number of rotations performed is from right side
  # and if n is negative then number of rotations performed from left side
  # Let's optimize the number of rotations.
  # Handle case if 'n' is a negative number.
  n = n % length

  if n < 0:
    n = n + length

  return n

def rotate_by_n(head, n):

    if n == 0:
        return head

    current = head

    length = find_length(head)

    # Calculate rotation to rotate from
    # If n (number of rotations required) is bigger than
    # length of linked list or if n is negative then
    # we need to adjust total number of rotations needed
    n = adjust_rotations_needed(n, length)
    # Find the start of rotated list.
    # If we have 1, 2, 3, 4, 5 where n = 2,
    # 4 is the start of rotated list.
    loc_to_rotate = length - n - 1

    first_node_of_previous_part = current
    previous = None

    # Traverse to the rotation location
    for i in range(1, loc_to_rotate):
        previous = current
        current = current.next
    
    # Last node of first part should point to None
    previous.next = None

    # Traverse the Second Part
    head = current
    while current.next:
        current = current.next
    current.next = first_node_of_previous_part

    return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
#   head.next.next.next.next.next = Node(6)
#   head.next.next.next.next.next.next = Node(7)
#   head.next.next.next.next.next.next.next = Node(8)
#   head.next.next.next.next.next.next.next.next = Node(9)
#   head.next.next.next.next.next.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate_by_n(head, 2)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()
