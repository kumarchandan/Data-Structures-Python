'''
Brute-force: O(n^2)
'''
from Stack import MyStack


def next_greater_element(lst):
    res = []
    # Iterate list
    for i in range(0, len(lst), 1):
        # initialise nextGreatest to -1
        next_greatest = -1
        for j in range(i+1, len(lst), 1):
            if lst[i] < lst[j]:
                # Update nextGreatest when greater value found
                next_greatest = lst[j]
                break
        # append next greatest
        res.append(next_greatest)
        print(str(lst[i]) + " -- " + str(next_greatest))
    return res


print(next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9]))
