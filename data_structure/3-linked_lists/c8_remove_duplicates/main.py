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

    prev_node = None
    curr_node = lst.get_head()
    while curr_node:
        if curr_node.data in visited_nodes:
            # delete it
            prev_node.next_element = curr_node.next_element
            curr_node.next_element = None
            curr_node = prev_node.next_element
        else:
            visited_nodes.append(curr_node.data)
            prev_node = curr_node
            curr_node = curr_node.next_element
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
