from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Node class attributes: {data, next_element}


def length(lst):
    # Write - Your - Code
    len_of_list = 0
    if lst.is_empty():
        return len_of_list
    
    curr_node = lst.get_head()
    while curr_node is not None:
        len_of_list += 1
        curr_node = curr_node.next_element

    return len_of_list
 
lst = LinkedList()
lst.insert_at_tail(10)
lst.insert_at_tail(11)
lst.insert_at_tail(12)
lst.insert_at_tail(30)
lst.print_list()

print('length of the list is: ', length(lst))