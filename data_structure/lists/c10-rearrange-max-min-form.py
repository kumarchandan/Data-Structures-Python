def max_min(lst):
    # Write your code here
    res = []
    mid = len(lst) // 2
    first_part = lst[0: mid]
    second_part = lst[mid: len(lst)]
    second_part.reverse()

    max_len = 0
    if len(first_part) > len(second_part):
        max_len = len(first_part)
    else:
        max_len = len(second_part)

    for i in range(max_len):
        try:
            res.append(second_part[i])
            res.append(first_part[i])
        except IndexError:
            continue
    return res

max_min([1, 2, 3, 4, 5, 6, 7])