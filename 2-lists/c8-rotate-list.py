def right_rotate(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

right_rotate([1, 2, 3, 4, 5], 2)