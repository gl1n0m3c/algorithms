def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def murge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = murge_sort(array[:middle])
    right = murge_sort(array[middle:])
    return merge_two_list(left, right)

array = [7, 5, 2, 3, 9, 8, 6]
print(*murge_sort(array))