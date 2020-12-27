from LinkedList import LinkedList
from Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Search for element => list.search()
# Node class  { int data ; Node next_element;}


def delete(lst, value):
    # Write your code here
    deleted = False
    prev_node = None

    if lst.is_empty():
        return deleted
    
    curr_node = lst.get_head()
    # case 1: to be deleted value is at head
    if curr_node.data is value:
        lst.delete_at_head()
        deleted = True
        return deleted

    # case 2: to be deleted value is not at head
    while curr_node is not None:
        if curr_node.data is value:
            prev_node.next_element = curr_node.next_element
            curr_node.next_element = None
            deleted = True
            break
        prev_node = curr_node
        curr_node = curr_node.next_element

    return deleted

lst = LinkedList()
lst.insert_at_tail(0)
lst.insert_at_tail(1)
lst.insert_at_tail(2)
lst.insert_at_tail(3)
lst.print_list()

print('delete 2')
delete(lst, 2)

print('after deletion:')
lst.print_list()