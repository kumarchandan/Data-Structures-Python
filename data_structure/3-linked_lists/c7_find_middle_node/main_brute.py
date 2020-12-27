from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def find_mid(lst):
    # Write your code here
    lst_len = lst.length()

    if lst_len % 2 == 0:
        mid = int(lst_len / 2)
    else:
        mid = int(1 + (lst_len // 2))
    
    curr = lst.get_head()
    for i in range(1, mid):
        curr = curr.next_element
    return curr.data

lst = LinkedList()
lst.insert_at_tail(10)
lst.insert_at_tail(9)
lst.insert_at_tail(4)
lst.insert_at_tail(6)
# lst.insert_at_tail(789)
lst.print_list()

print(find_mid(lst))
