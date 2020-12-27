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

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    curr_node = list1.get_head()
    while curr_node.next_element is not None:
        curr_node = curr_node.next_element

    # merge two linked list
    curr_node.next_element = list2.get_head()
    # remove duplicates
    list1.remove_duplicates()

    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here
    outer_node = list1.get_head()
    inner_node = None
    res = LinkedList()

    while outer_node:
        inner_node = list2.get_head()
        while inner_node:
            if outer_node.data == inner_node.data:
                # intersection found
                res.insert_at_tail(inner_node.data)
                break

            inner_node = inner_node.next_element
        outer_node = outer_node.next_element

    return res


lst1 = LinkedList()
lst1.insert_at_tail(10)
lst1.insert_at_tail(20)
lst1.insert_at_tail(80)
lst1.insert_at_tail(60)
lst1.print_list()

lst2 = LinkedList()
lst2.insert_at_tail(15)
lst2.insert_at_tail(20)
lst2.insert_at_tail(30)
lst2.insert_at_tail(60)
lst2.insert_at_tail(45)
lst2.print_list()

# print('Union:')
# union(lst1, lst2).print_list()

print('Intersection:')
intersection(lst1, lst2).print_list()
