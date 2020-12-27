from LinkedList import LinkedList

def find_mid(lst):
    if lst.is_empty():
        return -1
    
    curr_node = lst.get_head()
    # Case 1: if only one element in the linked list
    if curr_node.next_element is None:
        return curr_node.data
    
    # Case 2: General
    mid_node = lst.get_head()
    curr_node = curr_node.next_element.next_element

    while curr_node:
        mid_node = mid_node.next_element
        curr_node = curr_node.next_element
        if curr_node:
            curr_node = curr_node.next_element
    if mid_node:
        return mid_node.data
    return -1


lst = LinkedList()
lst.insert_at_tail(10)
lst.insert_at_tail(9)
lst.insert_at_tail(4)
lst.insert_at_tail(6)
# lst.insert_at_tail(78)
lst.print_list()

print(find_mid(lst))
