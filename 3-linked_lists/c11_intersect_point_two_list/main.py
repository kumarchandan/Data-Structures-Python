from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}


def intersect(head1, head2):
  #TODO: Write - Your - Code
  intersect_node = None
  outer_node = head1
  inner_node = None
  while outer_node:
    inner_node = head2
    while inner_node:
      if inner_node is outer_node:
        intersect_node = inner_node
        return intersect_node
      inner_node = inner_node.next_element
    outer_node = outer_node.next_element
  return intersect_node


lst1 = LinkedList()
lst1.insert_at_tail(13)
lst1.insert_at_tail(4)
lst1.insert_at_tail(12)
lst1.insert_at_tail(27)
lst1.print_list()

lst2 = LinkedList()
lst2.insert_at_tail(24)
lst2.insert_at_tail(23)
lst2.insert_at_tail(82)
lst2.insert_at_tail(11)
lst2.insert_at_tail(12)
lst2.insert_at_tail(27)
lst2.print_list()

for i in range(1, 6)

print('Any intersection point:')
print(intersect(lst1.get_head(), lst2.get_head()))
