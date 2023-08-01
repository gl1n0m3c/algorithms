def sorting_by_choice(array):
    if len(array) == 1:
        return array
    else:
        for i in range(len(array) - 1):
            index_of_min_element = i
            for j in range(i + 1, len(array)):
                if array[index_of_min_element] > array[j]:
                    index_of_min_element = j
            array[i], array[index_of_min_element] = array[index_of_min_element], array[i] 
    return array

array = [5, -1, 8, 2, -6, -11, 215]
print(sorting_by_choice(array))