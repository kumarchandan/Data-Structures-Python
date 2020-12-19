def merge_lists(lst1, lst2):
    # Write your code here
    res = []
    # handle case where one of the list will be empty
    if len(lst1) == 0 or len(lst2) == 0:
        res.extend(lst1 + lst2)
        return res
    
    last_processed_i_idx = 0
    last_processed_j_idx = 0
    for i_idx, i in enumerate(lst1):
        for j_idx, j in enumerate(lst2, start=last_processed_j_idx + 1):
            if i < j:
                res.append(i)
                last_processed_i_idx = i_idx
                break
            elif i > j:
                res.append(j)
                last_processed_j_idx = j_idx
                continue
            else:
                res.append(i)
                last_processed_i_idx = i_idx
                res.append(j)
                last_processed_j_idx = j_idx
                break
    
    if len(lst1) == last_processed_i_idx:
        res.extend(lst2[last_processed_j_idx + 1:])
    
    if len(lst2) == last_processed_j_idx:
        res.extend(lst1[last_processed_i_idx+ 1:])
    return res

print(merge_lists([1, 3, 4, 5], [2, 6, 7, 8]))
# print(merge_lists([], []))
