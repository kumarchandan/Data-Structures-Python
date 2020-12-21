from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}

def remove_duplicates(lst):
    # Write - Your - Code
    visited_nodes = []

    outer_node = lst.get_head()
    inner_node = None
    prev_node = None

    while outer_node:
        inner_node = outer_node.next_element
        prev_node = outer_node
        while inner_node:
            if inner_node.data is outer_node.data:
                # remove it
                prev_node.next_element = inner_node.next_element
                inner_node.next_element = None
                inner_node = prev_node.next_element
            else:
                prev_node = inner_node
                inner_node = inner_node.next_element
        outer_node = outer_node.next_element
    return




lst = LinkedList()
lst.insert_at_tail(7)
lst.insert_at_tail(14)
lst.insert_at_tail(21)
lst.insert_at_tail(14)
lst.insert_at_tail(22)
lst.insert_at_tail(7)
lst.insert_at_tail(21)
lst.print_list()

remove_duplicates(lst)
print('After removal of duplicates')
lst.print_list()
