def heapify(arr: list, n: int, i: int):
    l = 2 * i + 1  # левый потомок
    r = 2 * i + 2  # правый потомок

    largest = i  # считаем, что индекс наибольшего эл-та равен i
 
    # проверим, существует ли левый потомок
    if l < n and arr[l] > arr[largest]:
        largest = l

    # проверим, существует ли правый потомок
    if r < n and arr[r] > arr[largest]:
        largest = r

    # заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n , largest)

def heapSort(arr):
    n = len(arr)

    # построение кучи
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)

A = [10, 5, 4, 3, 7, 11, 2, 5, 21]

heapSort(A)

print(*A)
