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

# Function to find the nth node from end of Linked List


def find_nth(lst, n):
    # Write your code here
    
    lst_len = lst.length()
    len_frm_start = lst_len - n

    if len_frm_start < 1:
        return -1
    
    curr = lst.get_head()

    for i in range(1, len_frm_start + 1):
        curr = curr.next_element

    return curr.data


lst = LinkedList()
lst.insert_at_tail(15)
lst.insert_at_tail(20)
lst.insert_at_tail(30)
lst.insert_at_tail(60)
lst.insert_at_tail(45)
lst.print_list()

find_nth(lst, 2)
