from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list


def insert_at_tail(lst, value):
    # Write - Your - Code
    new_node = Node(value)

    if lst.is_empty():
        lst.head_node = new_node
        return

    temp = lst.get_head()
    while temp.next_element is not None:
        temp = temp.next_element
        
    temp.next_element = new_node
    return

lst = LinkedList()
lst.print_list()
insert_at_tail(lst, 0)
lst.print_list()
insert_at_tail(lst, 1)
lst.print_list()
insert_at_tail(lst, 2)
lst.print_list()
insert_at_tail(lst, 3)
lst.print_list()