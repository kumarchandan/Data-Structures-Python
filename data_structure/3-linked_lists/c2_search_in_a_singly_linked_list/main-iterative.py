from LinkedList import LinkedList
from Node import Node


def search(lst, value):

    # Start from first element
    current_node = lst.get_head()

    # Traverse the list till you reach end
    while current_node:
        if current_node.data is value:
            return True  # value found
        current_node = current_node.next_element

    return False  # value not found


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(40)
lst.insert_at_head(5)
lst.print_list()
print(search(lst, 4))
