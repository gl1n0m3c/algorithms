def quick_sotr(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greatest = [i for i in array[1:] if i > pivot]
    return quick_sotr(less) + [pivot] + quick_sotr(greatest)
print(quick_sotr([10, 5, 2, 3]))