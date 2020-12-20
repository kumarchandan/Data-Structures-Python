from Node import Node
from LinkedList import LinkedList
#Access head_node => list.get_head()
#Check if list is empty => list.is_empty()
#Delete at head => list.delete_at_head()
#Delete by value => list.delete(value)
#Search for element => list.search()
#Length of the list => list.length()
#Node class  { int data ; Node next_element;}

def reverse(lst):
  # Write your code here
  prev = None
  curr = lst.get_head()
  next = None

  while curr:
    next = curr.next_element
    curr.next_element = prev
    prev = curr
    curr = next
  
    lst.head_node = prev

  return lst


lst = LinkedList()
lst.insert_at_tail(10)
lst.insert_at_tail(9)
lst.insert_at_tail(4)
lst.insert_at_tail(6)
lst.print_list()

reversed_lst = reverse(lst)
print('Reversed linked list:')
reversed_lst.print_list()